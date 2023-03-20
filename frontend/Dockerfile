# Use the official Node.js base image
FROM node:16

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json into the container
COPY package*.json ./

# Install any needed packages specified in package.json
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the app
RUN npm run build

# Use the official Nginx base image
FROM nginx:1.21

# Copy the build output to replace the default Nginx contents
COPY --from=0 /app/dist /usr/share/nginx/html

# Expose port 80
EXPOSE 80
