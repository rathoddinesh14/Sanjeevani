#!/bin/bash

# Function to check if a command exists
command_exists () {
    command -v "$1" >/dev/null 2>&1 ;
}

# Check if Java is installed, if not, install it
if command_exists java ; then
    echo "Java is already installed."
else
    echo "Java not found. Installing OpenJDK 11..."
    sudo apt install -y openjdk-11-jdk
fi

# Check if Zookeeper is installed, if not, install it
if command_exists zookeeper-server-start ; then
    echo "Zookeeper is already installed."
else
    echo "Zookeeper not found. Installing Zookeeper..."
    sudo apt install -y zookeeperd
    sudo systemctl enable zookeeper
    sudo systemctl start zookeeper
fi

# # Download Kafka
# KAFKA_VERSION="3.8.0"
# KAFKA_SCALA_VERSION="2.13"
# KAFKA_DOWNLOAD_URL="https://dlcdn.apache.org/kafka/${KAFKA_VERSION}/kafka_${KAFKA_SCALA_VERSION}-${KAFKA_VERSION}.tgz"

# echo "Downloading Kafka version $KAFKA_VERSION..."
# wget $KAFKA_DOWNLOAD_URL -O /tmp/kafka.tgz

# # Extract Kafka
# echo "Extracting Kafka..."
# sudo mkdir -p /opt/kafka
# sudo tar -xvzf /tmp/kafka.tgz --strip 1 -C /opt/kafka

# # Remove the downloaded tar file
# rm /tmp/kafka.tgz

# # Configure Kafka environment
# echo "Configuring Kafka environment..."
# echo "export KAFKA_HOME=/opt/kafka" >> ~/.bashrc
# echo "export PATH=\$PATH:\$KAFKA_HOME/bin" >> ~/.bashrc
# source ~/.bashrc

# Start Zookeeper (in case it's not running)
echo "Starting Zookeeper service..."
sudo systemctl start zookeeper

# Start Kafka server
echo "Starting Kafka broker..."
sudo /opt/kafka/bin/kafka-server-start.sh -daemon /opt/kafka/config/server.properties

echo "Kafka installation complete. Kafka is now running."
