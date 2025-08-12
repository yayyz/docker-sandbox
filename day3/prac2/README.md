# 실습 #2
### 목표
Python Flask 애플리케이션이 Redis 캐시 서버와 통신 할 수 있도록 이 두서비스를 docker-compose로 실행해주세요!

### 요구사항 
Python Flask App:
- redis의 상태에 의존되도록 설정해주세요
- 내부포트: 5000
- 볼륨 마운트: /app
- command:  sh -c "pip install flask redis && python app.py"

Redis:
- 내부포트: 6379
- redis의 상태가 python container와 공유될 수 있도록 healthcheck 설정을 추가해주세요
- 볼륨 마운트: /data

### 제출방법
1. 이 repo (docker-sandbox)를 [Fork](https://github.com/yayyz/docker-sandbox/fork) 해주세요
2. Forked된 Repo에서 본인 이름의 브랜치를 추가해주세요
3. 본인 이름의 브랜치에서 docker-compose.yml를 업데이트 해주세요 (git push)
4. yayyz/docker-sandbox로 Pull Request를 날려주세요! 
