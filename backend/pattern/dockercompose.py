base = '''version: '3'
services:\n\n'''

nginx = '''  nginx:
    image: nginx:stable
    volumes:
      - "/mnt/frontend/conf/nginx/etc/nginx:/etc/nginx"
      - "/mnt/frontend/log/nginx:/var/log/nginx"
    ports:
      - "80:80"
      - "443:443"'''

adminer = '''  pma:
    image: adminer:latest
    ports:
      - "8081:8080"\n\n'''
      
web = '''  web:
    build:
      context: %s
      dockerfile: Dockerfile
    environment:
      OPENSSL_CONF: /usr/local/ssl/openssl.cnf
    volumes:
      - "/mnt/frontend/www:/var/www"
    ports:
      - "8080:80"
    depends_on:
      - nginx\n\n'''
      
dbps = '''  db:
    image: postgres:12
    environment:
      - POSTGRES_PASSWORD=%s
    volumes:
      - "/mnt/frontend/postgresql /var/lib/postgresql/ "
      - "/mnt/frontend/pos.cnf:/etc/pos.cnf"
    ports:
      - "3306:5432"\n\n'''
      
dbmy = '''  db:
    image: mariadb:10.3
    environment:
      - ROOT_PASSWORD=%s
    volumes:
      - "/mnt/frontend/mysql /var/lib/mysql/ "
      - "/mnt/frontend/my.cnf:/etc/my.cnf"
    ports:
      - "3306:3306"\n\n'''