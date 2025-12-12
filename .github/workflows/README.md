# 📧 Email Header Processor (Web Edition)

A browser-based tool to process email headers for support tickets. Based on the original Python script, but now running entirely in your browser!

## ✨ Features

- **No installation required** - Works in any modern web browser
- **Complete privacy** - All processing happens locally, no data is sent to servers
- **One-click processing** - Simple, intuitive interface
- **Multiple output options** - Copy to clipboard or download as file
- **Real-time statistics** - See exactly what was changed

## 🚀 Live Demo

Access the tool directly at: `https://YOUR_USERNAME.github.io/email-header-processor`

## 🛠️ What It Does

1. **Removes sensitive headers**: Received, Return-Path, DKIM-Signature, ARC headers, etc.
2. **Anonymizes domains**: Changes `.fin` to `.[RDNS]` in From field
3. **Adds tracking ID**: Inserts `[EID]` to Message-ID field
4. **Preserves other headers**: All other information remains unchanged

## 📁 File Structure
