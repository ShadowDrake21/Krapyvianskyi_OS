FROM jenkins/jenkins:latest

USER root

# Install additional packages if needed
RUN apt-get update && apt-get install -y \
    rpm \
    fakeroot \
 && rm -rf /var/lib/apt/lists/*

USER jenkins

# Expose the default Jenkins web port
EXPOSE 8080

ENV JENKINS_OPTS="--prefix=/jenkins"

# Start Jenkins
CMD ["/usr/local/bin/jenkins.sh"]
