FROM node:20-alpine

WORKDIR /app

COPY package.json /app/package.json
COPY packages/shared /app/packages/shared
COPY apps/web /app/apps/web

RUN npm install

EXPOSE 3000

CMD ["npm", "run", "dev:web", "--", "--hostname", "0.0.0.0"]
