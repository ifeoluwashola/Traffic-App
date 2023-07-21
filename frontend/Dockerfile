# Base image
FROM node:16

# Set working directory in the Docker image
WORKDIR /traffic-app

# Copy package.json and package-lock.json (if available) to the workdir in Docker image
COPY traffic-app/package*.json ./

# Install dependencies in the Docker image
RUN npm install

# Copy the rest of the application to the Docker image
COPY  traffic-app/ .

# Build the application
RUN npm run build

# The app runs on port 3000
EXPOSE 3000

# Start the application
CMD ["npm", "start"]
