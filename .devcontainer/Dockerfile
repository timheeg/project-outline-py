ARG BASE_IMAGE_NAME
ARG BASE_IMAGE_TAG
FROM $BASE_IMAGE_NAME:$BASE_IMAGE_TAG

# Provide your own RHEL subscription
RUN --mount=type=secret,id=RHEL8_ORG \
  --mount=type=secret,id=RHEL8_ACTIVATION_KEY \
  subscription-manager register \
  --org=$(cat /run/secrets/RHEL8_ORG) \
  --activationkey=$(cat /run/secrets/RHEL8_ACTIVATION_KEY)

# Install tools
#
# python, pip latest
# vim-enhanced for color vi support in git
#
RUN dnf update -y \
  && dnf -y install \
  git \
  python3.12 \
  python3.12-pip \
  unzip \
  vim-enhanced \
  zip \
  && dnf clean all \
  && rm -rf /var/cache/yum

  # Install root user .bashrc
COPY .bashrc /root/

# 🧑‍💻 Create the developer (non-root) user
ARG USERNAME
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user and group
# Don't add sudo to build container
RUN groupadd --gid $USER_GID $USERNAME \
  && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME

# Install the .bashrc for the user
COPY .bashrc /home/$USERNAME
RUN chown $USER_UID:$USERNAME "/home/$USERNAME/.bashrc" \
  && chmod 644 "/home/$USERNAME/.bashrc"

# Change default user (to you) for the remainder
USER $USERNAME

# Create python venv for non-root user
RUN python3 -m venv /home/$USERNAME/env

CMD [ "bash" ]
