# Use the official Node.js 18 Alpine image as a base image
FROM node:18-alpine

# Set the working directory to /app within the container
WORKDIR /app

# Copy all files from the local frontend directory to /app in the container
COPY . .

# Install all dependencies defined in package.json
RUN npm install

# Build the Next.js application
RUN npm run build

# Expose port 3000 to be accessible from outside the container
EXPOSE 3000

# Start the Next.js application
CMD ["npm", "start"]
