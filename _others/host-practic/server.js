const express = require('express');
const app = express();

// Whitelist — allowed hosts (without port)
const allowedHosts = new Set(['site1.local', 'site2.local', 'localhost']);

// Normalize host: remove port and convert to lowercase
function normalizeHost(raw) {
  if (!raw) return '';
  return raw.split(':')[0].toLowerCase();
}

// Basic check to ensure Host header does not contain CR/LF/whitespace
// and consists of valid characters (letters, digits, hyphen, dot, optional :port)
function isSafeHost(raw) {
  if (!raw) return false;
  // Block newline, carriage return, tab, and all whitespace characters
  if (/[\r\n\t\s]/.test(raw)) return false;
  // Validate format: example.com or example.com:3000
  return /^[a-z0-9.-]+(:[0-9]+)?$/i.test(raw);
}

// Log all incoming requests and Host header for debugging
app.use((req, res, next) => {
  console.log('--- Request ---');
  console.log('Host header (raw):', req.headers.host);
  console.log('URL:', req.originalUrl);
  console.log('Method:', req.method);
  next();
});

app.get('/', (req, res) => {
  const rawHost = req.headers.host || '';

  // Security: reject "unsafe" Host headers
  if (!isSafeHost(rawHost)) {
    console.log('Blocked unsafe Host header:', JSON.stringify(rawHost));
    return res.status(400).send('Invalid Host header');
  }

  const host = normalizeHost(rawHost);

  // Enforce whitelist — only allow known hosts
  if (!allowedHosts.has(host)) {
    console.log('Blocked unallowed Host:', host);
    return res.status(400).send('Invalid Host header');
  }

  // Serve content based on Host
  if (host === 'site1.local') return res.send('Hello from SITE 1!');
  if (host === 'site2.local') return res.send('Hello from SITE 2!');
  return res.send('Hello from DEFAULT site!');
});

// Start server on port 3000
app.listen(3000, () => console.log('Server on http://127.0.0.1:3000'));
