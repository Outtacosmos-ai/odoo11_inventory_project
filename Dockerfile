FROM odoo:11

USER root

# Install additional dependencies if needed
RUN apt-get update && apt-get install -y --no-install-recommends     python3-pip     && rm -rf /var/lib/apt/lists/*

# Install any Python packages required by your custom modules
# RUN pip3 install some-package

# Copy custom addons
COPY ./addons /mnt/extra-addons

# Copy Odoo configuration
COPY ./config /etc/odoo

# Set permissions
RUN chown -R odoo:odoo /mnt/extra-addons /etc/odoo

# Switch back to odoo user
USER odoo
