FROM relaysh/core:latest-python
RUN pip install pdpyras
COPY "./step.py" "/entrypoint.py"
ENTRYPOINT []
CMD ["python3", "/entrypoint.py"]

LABEL "org.opencontainers.image.title"="VictorOps Incident update"
LABEL "org.opencontainers.image.description"="This step updates an incident in VictorOps"
LABEL "com.puppet.nebula.sdk.version"="v1"
