# Learning-Container
---
1. Why we have to use container
    1. 배경
    2. VMware, VBox
    3. 컨테이너
    4. 컨테이너의 원리
        1. cgroups
        2. Linux Namespace
    5. 성능의 차이
2. Development Environment
    1. Monolithic architecture
    2. Microservice architecture(MSA)
3. Docker Installation
    1. Docker
    2. 도커와 사용가능한 클라우드 서비스 모델
    3. 도커의 한계
    4. Docker의 이상적 동작 환경은 Linux
4. Docker registry
    1. Docker registry
    2. 원하는 Image를 Pull하는 방법
    3. 로컬 시스템에 있는 Image
5. Docker life cycle
    1. Docker life cycle
    2. 명령어
        1. Image pulling and removing
        2. Creating and starting(Run) container
        3. 컨테이너 확인
        4. 컨테이너 중지
        5. 컨테이너 삭제
    3. 사용 예제
6. Layer and File system
    1. Layer
    2. Image information
    3. Docker data management
7. Docker docs
    1. $ docker --help
    2. Some useful command in Docker
        1. docker run
        2. docker exec -it tc /bin/bash
        3. docker logs \[CONTAINER_NAME\]
        4. File transfer between host and container or between containers
        5. Removing all container
    3. 볼륨 마운트
8. Building image
    1. Echo-server with python:3.8.2
    2. Dockerfile and build
    3. Image 경량화
        1. Use minimal base image
        2. Reduce number of image layers
        3. Move user application code to below
        4. Multi-stage build
        5. Use .dockerignore file
9. Push to dockerhub
    1. Setting docker image to push
    2. Push
    3. History of image