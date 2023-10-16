# gohan_map-backend

### 環境

Python 3.10  
Poetry

### 起動方法(開発環境)

- .env.sample を.env にコピーする
- firebaseAdminKey.json をルートに配置する(開発者に相談)

```bash
docker compose -f docker-compose.local.yml up -d

poetry install
poetry shell
poe serve
```
