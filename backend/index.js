const express = require('express');
const axios = require('axios');
const cors = require('cors');
require('dotenv').config();

const app = express();
app.use(express.json());
app.use(cors());

// Webhook و API Key يتم قراءتها من متغيرات البيئة
const webhookUrl = process.env.DISCORD_WEBHOOK;
const binId = process.env.BIN_ID;
const apiKey = process.env.API_KEY;

// إرسال رسالة للديسكورد
app.post('/send-support', async (req, res) => {
    try {
        const { content } = req.body;
        await axios.post(webhookUrl, { content });
        res.json({ ok: true });
    } catch (e) {
        res.status(500).json({ ok: false });
    }
});

// التعامل مع JSONBin
app.get('/get-entries', async (req, res) => {
    try {
        const resp = await axios.get(`https://api.jsonbin.io/v3/b/${binId}/latest`, {
            headers: { "X-Master-Key": apiKey }
        });
        res.json(resp.data);
    } catch (e) {
        res.status(500).json({ ok: false });
    }
});

app.put('/save-entries', async (req, res) => {
    try {
        await axios.put(`https://api.jsonbin.io/v3/b/${binId}`, req.body, {
            headers: {
                "Content-Type": "application/json",
                "X-Master-Key": apiKey
            }
        });
        res.json({ ok: true });
    } catch (e) {
        res.status(500).json({ ok: false });
    }
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log("Backend running on port " + PORT));
