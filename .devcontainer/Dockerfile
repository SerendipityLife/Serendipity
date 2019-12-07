FROM amazonlinux:2.0.20191016.0

ARG USERNAME="vscode"
ARG USER_UID=1000
ARG USER_GID=${USER_UID}
ARG USER_HOME=/home/${USERNAME}

ENV APP_HOME=${USER_HOME}/app

RUN yum update -y \
    # Install middlewares and modules
    && yum install shadow-utils tar sudo git procps python3.7.4 python3-pip -y \
    # Set up user config
    && groupadd --gid ${USER_GID} ${USERNAME}  \
    && useradd -c "vscode app user" -m -s /bin/bash --uid ${USER_UID} --gid ${USER_GID} ${USERNAME} \
    && sudo -u ${USERNAME} mkdir ${APP_HOME} \
    && chown -R ${USERNAME}:${USERNAME} ${USER_HOME} \
    && chmod -R 0775 ${USER_HOME} \
    && usermod -aG adm ${USERNAME} \
    && echo ${USERNAME} ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME\
    && chmod 0440 /etc/sudoers.d/${USERNAME} \
    # Cache clean
    && yum clean all -y \
    && rm -rf  /var/cache/yum \
    ;

# USER ${USERNAME}