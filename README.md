# TicTacToe — Human vs Bot (DevOps demo)

Demo project that showcases a small production-like stack:
- Flask backend (Python)
- Redis (for active games in more advanced variants)
- Postgres (store completed games)
- Docker + Docker Compose for local reproduction
- GitHub Actions CI: tests + Docker image build
- Simple browser UI (vanilla JS)

## Quick start (local)

Requirements: Docker & docker-compose

```bash
# clone repo
git clone <your-repo-url>
cd tictactoe-devops

# build & run (first time will initialize DB)
docker-compose up --build
