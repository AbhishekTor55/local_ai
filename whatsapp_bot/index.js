const { Client } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');
const axios = require('axios');

const client = new Client();

client.on('qr', qr => {
    qrcode.generate(qr, { small: true });
    console.log("Scan QR with WhatsApp");
});

client.on('ready', () => {
    const myNumber = client.info.wid.user; // phone number
    console.log("✅ WhatsApp connected");
    console.log(`📱 Active WhatsApp Number: +${myNumber}`);
    console.log("👉 Use THIS number's 'Message yourself' chat to talk with OpenClaw AI");
});


// 🔥 IMPORTANT FIX HERE
client.on('message_create', async msg => {
    console.log("DEBUG → fromMe:", msg.fromMe);
    console.log("DEBUG → text:", msg.body);

    if (!msg.fromMe) return;

    // Debug ONLY for self-chat
    console.log("SELF CHAT →", msg.body);

    try {
        const res = await axios.post("http://127.0.0.1:5000/chat", {
            text: msg.body,
            source: "whatsapp"
        });

        await msg.reply(res.data.reply);
    } catch (err) {
        console.error("AI ERROR:", err.message);
    }
});

client.initialize();
