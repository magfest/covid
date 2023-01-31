FROM ghcr.io/magfest/ubersystem:west2022

# add our code
COPY . plugins/covid/
RUN if [ -d plugins/covid/plugins ]; then mv plugins/covid/plugins/* plugins/; fi
RUN /app/env/bin/paver install_deps
