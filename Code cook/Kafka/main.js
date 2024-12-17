const { Kafka } = require("kafkajs");

const kafka = new Kafka({
  clientId: "my-app",
  brokers: ["127.0.0.1:9001", "127.0.0.1:9002", "127.0.0.1:9003"],
  sasl: {
    mechanism: "plain",
    username: "CtelRnDDefaultUser",
    password: "CtelRnDDefaultUserPassword",
  },
});

const main = async () => {
  try {
    const topic = "test-topic";

    // Create Producer and Consumer
    const producer = kafka.producer();
    const consumer = kafka.consumer({ groupId: "test-group" });

    // Connect Producer and Consumer
    await producer.connect();
    await consumer.connect();
    await consumer.subscribe({ topic, fromBeginning: true });

    // Producer Logic
    const produceMessage = async () => {
      const messageValue = `Message at ${new Date().toISOString()}`;
      await producer.send({
        topic,
        messages: [{ value: messageValue }],
      });
      console.log(`Produced: ${messageValue}`);
    };

    // Consumer Logic
    await consumer.run({
      eachMessage: async ({ topic, partition, message }) => {
        const prefix = `${topic}[${partition} | ${message.offset}] / ${message.timestamp}`;
        console.log(
          `Consumed: ${prefix} ${message.key || ""}#${message.value}`
        );
      },
    });

    // Set interval for producing messages every 3 seconds
    setInterval(() => {
      produceMessage().catch((e) =>
        console.error(`[example/producer] ${e.message}`, e)
      );
    }, 500);

    // Handle errors and signals
    const errorTypes = ["unhandledRejection", "uncaughtException"];
    const signalTraps = ["SIGTERM", "SIGINT", "SIGUSR2"];

    errorTypes.forEach((type) => {
      process.on(type, async (e) => {
        try {
          console.log(`process.on ${type}`);
          console.error(e);
          await producer.disconnect();
          await consumer.disconnect();
          process.exit(0);
        } catch (_) {
          process.exit(1);
        }
      });
    });

    signalTraps.forEach((type) => {
      process.once(type, async () => {
        try {
          await producer.disconnect();
          await consumer.disconnect();
        } finally {
          process.kill(process.pid, type);
        }
      });
    });
  } catch (error) {
    console.error("Error connecting Kafka: ", error);
  }
};

main();
