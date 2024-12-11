const { Kafka } = require("kafkajs");

const kafka = new Kafka({
  clientId: "my-app",
  brokers: ["127.0.0.1:9001", "127.0.0.1:9002", "127.0.0.1:9003"],
  // sasl: {
  //   mechanism: "plain",
  //   username: "user",
  //   password: "user-secret",
  // },
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
    }, 3000);

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




- KAFKA_CFG_NODE_ID=0
- KAFKA_CFG_PROCESS_ROLES=controller,broker
- KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=0@10.60.68.77:9093,1@10.60.68.116:9093,2@10.60.68.163:9093
- KAFKA_KRAFT_CLUSTER_ID=abcdefghijklmnopqrstuv
- KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093,SASL_PLAINTEXT://:9094
- KAFKA_CFG_ADVERTISED_LISTENERS=SASL_PLAINTEXT://127.0.0.1:9094,PLAINTEXT://10.60.68.77:9092
- KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=PLAINTEXT:PLAINTEXT,CONTROLLER:PLAINTEXT,SASL_PLAINTEXT:SASL_PLAINTEXT
- KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER
- KAFKA_CFG_SECURITY_INTER_BROKER_PROTOCOL=PLAINTEXT
- KAFKA_CFG_SASL_ENABLED_MECHANISMS=PLAIN
- KAFKA_CFG_SASL_MECHANISM_INTER_BROKER_PROTOCOL=PLAIN
- KAFKA_OPTS=-Djava.security.auth.login.config=/opt/bitnami/kafka/config/kafka_jaas.conf


KAFKA_CFG_NODE_ID=0
KAFKA_CFG_PROCESS_ROLES=controller,broker
KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=0@10.60.68.77:9093,1@10.60.68.116:9093,2@10.60.68.163:9093
KAFKA_KRAFT_CLUSTER_ID=abcdefghijklmnopqrstuv
KAFKA_CFG_LISTENERS=CONTROLLER://:9093,SASL_PLAINTEXT://:9094
KAFKA_CFG_ADVERTISED_LISTENERS=CONTROLLER://10.60.68.77:9093,SASL_PLAINTEXT://10.60.68.77:9094
KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,SASL_PLAINTEXT:SASL_PLAINTEXT
KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER
KAFKA_CFG_SECURITY_INTER_BROKER_PROTOCOL=PLAINTEXT
KAFKA_CFG_SASL_ENABLED_MECHANISMS=PLAIN
KAFKA_CFG_SASL_MECHANISM_INTER_BROKER_PROTOCOL=PLAIN
KAFKA_OPTS=-Djava.security.auth.login.config=/opt/bitnami/kafka/config/kafka_jaas.conf

KAFKA_CFG_LISTENERS=CONTROLLER://:9093,SASL_PLAINTEXT://:9094
KAFKA_CFG_ADVERTISED_LISTENERS=CONTROLLER://10.60.68.77:9093,SASL_PLAINTEXT://10.60.68.77:9094
KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,SASL_PLAINTEXT:SASL_PLAINTEXT
KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER


{'KAFKA_CFG_PROCESS_ROLES': 'controller, broker', 'KAFKA_CFG_CONTROLLER_LISTENER_NAMES': 'CONTROLLER', 'KAFKA_CFG_BROKER_ID': '0', 'KAFKA_CFG_NODE_ID': '0', 'KAFKA_KRAFT_CLUSTER_ID': '7dabb370-68e6-4735-bf3e-c86ecafe1687', 'KAFKA_CFG_LISTENERS': 'CONTROLLER://:9093,SASL_PLAINTEXT://:9092', 'KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP': 'CONTROLLER:PLAINTEXT,SASL_PLAINTEXT:SASL_PLAINTEXT', 'KAFKA_CFG_CONTROLLER_QUORUM_VOTERS': '0@10.60.68.163:9093,1@10.60.68.116:9093,2@10.60.68.77:9093', 'KAFKA_CFG_ADVERTISED_LISTENERS': 'SASL_PLAINTEXT://10.60.68.163:9092', 'KAFKA_CFG_SASL_ENABLED_MECHANISMS': 'PLAIN', 'KAFKA_CFG_SASL_MECHANISM_INTER_BROKER_PROTOCOL': 'PLAIN', 'KAFKA_CFG_SECURITY_INTER_BROKER_PROTOCOL': 'SASL_PLAINTEXT', 'KAFKA_CFG_SUPER_USERS': 'User:admin', 'KAFKA_OPTS': '-Djava.security.auth.login.config=/opt/bitnami/kafka/config/kafka_jaas.conf', 'JMX_PORT': 2020, 'EXTRA_ARGS': '-javaagent:/jmx/jmx_prometheus_javaagent-1.0.1.jar=7071:/jmx/config.yaml', 'KAFKA_CFG_AUTO_CREATE_TOPICS_ENABLE': 'true'}