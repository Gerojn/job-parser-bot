# Job Parser Bot

Telegram bot for showing job vacancies.

## Features

- `/start` command
- `/help` command
- button for showing vacancies
- mock job data
- project structure with handlers, keyboards, and services
- environment variables with `.env`

## Tech Stack

- Python
- aiogram
- uv
- python-dotenv

## Installation

1. Clone the repository
2. Install dependencies
3. Create `.env`
4. Add your bot token
5. Run the bot

## Commands

- `/start` — start the bot  
- `/help` — show help  
- `Показати вакансії` — show available jobs  

## Run

```bash
uv sync
uv run python main.py

Environment Variables:
Create .env file:
BOT_TOKEN=your_bot_token_here

Future Improvements
real job parser
database integration
filters by keyword
saving user requests