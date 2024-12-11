const amqp = require("amqplib");

// Cấu hình kết nối
const config = {
  protocol: "amqp",
  hostname: "127.0.0.1",
  port: 5672,
  username: "guest", // username mặc định
  password: "guest", // password mặc định
  vhost: "/",
};

// Hàm kết nối và gửi message
async function connectQueue() {
  try {
    // Tạo kết nối
    const connection = await amqp.connect(config);
    console.log("Connection to RabbitMQ created successfully");

    // Tạo channel
    const channel = await connection.createChannel();
    console.log("Channel created successfully");

    // Tên queue
    const queueName = "test_queue";

    // Đảm bảo queue tồn tại
    await channel.assertQueue(queueName);

    // Gửi message
    const message = "Hello from Node.js!";
    channel.sendToQueue(queueName, Buffer.from(message));
    console.log(`Sent message: ${message}`);

    // Consumer để nhận message
    channel.consume(queueName, (data) => {
      console.log(`Received: ${data.content}`);
      channel.ack(data);
    });

    // Xử lý đóng kết nối
    process.on("exit", (code) => {
      channel.close();
      console.log(`Closing channel and connection`);
    });
  } catch (error) {
    console.error("Error:", error);
  }
}

// Chạy hàm kết nối
connectQueue();
