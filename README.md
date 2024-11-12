# Odoo 11 Custom Inventory Adjustment Project

This project enhances the Inventory Adjustments feature within the Inventory module of Odoo 11.

## Features

- Custom user group for Inventory Adjustment Managers
- Enhanced views for Inventory Adjustments
- Dockerized setup for easy deployment and development

## Prerequisites

- Docker
- Docker Compose

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/your-repo/odoo11_inventory_project.git
   cd odoo11_inventory_project
   ```

2. Build and start the Docker containers:
   ```
   docker-compose up -d
   ```

3. Access Odoo at `http://localhost:8069`

4. Create a new database and install the `custom_inventory_adjustment` module.

## Usage

1. Log in as an administrator.
2. Go to Settings > Users > Groups and assign users to the "Inventory Adjustment Manager" group.
3. Access the custom Inventory Adjustments feature from the Inventory module.

## Development

To modify or extend the custom module:

1. Edit files in the `addons/custom_inventory_adjustment` directory.
2. Restart the Odoo container to reflect changes:
   ```
   docker-compose restart web
   ```

## Logging

Logs are stored in the `./logs` directory. You can view them using:

```
tail -f logs/odoo-server.log
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the LGPL License - see the [LICENSE.md](LICENSE.md) file for details.
