# Apache Pulsar Setup Requirements for 50,000 Messages/Second

## 1. Broker and Bookie Recommendations
To handle **50,000 messages per second** with a message size of **1.5 KB**, the following setup is recommended:

- **Brokers**: 3–5 brokers to handle the load effectively. Each broker can manage multiple topics and subscriptions, ensuring that consumers can read from different partitions efficiently.
- **Bookies**: 3–5 bookies to provide sufficient storage and redundancy. Pulsar's architecture allows it to scale horizontally, so starting with 3 bookies and increasing as necessary based on performance metrics is beneficial.

### Calculation for Required Bookies
- With a message size of **1.5 KB**, storing messages for **1 day** for **50,000 messages/second** translates to:
  - Total messages per day: 50,000 * 60 * 60 * 24 = 4,320,000,000 messages
  - Total storage per day: 4,320,000,000 * 1.5 KB / 1024 = ~6,157,657.43 MB (~6 TB)

This storage does not include overheads, so it’s advisable to provision more disk space to accommodate growth and performance metrics.

## 2. Disk Space Requirements
To store messages for **1 day**:
- Provision at least **8 TB** of disk space to account for overhead and any additional storage needs. Using durable and reliable storage (e.g., SSDs) is crucial for performance and availability.

## 3. Retention Policy
For message deletion:
- Set the retention policy to delete messages after **1 day**. Use the following configuration command in Pulsar:
  ```
  pulsar-admin topics set-retention <topic-name> --size -1 --time 1d
  ```
This configuration ensures that messages older than **1 day** are automatically deleted. 

## 4. Node Configuration
A recommended configuration for each **Broker** and **Bookie** node:
- **CPUs**: 4–8 cores (more may be needed for higher throughput)
- **RAM**: 16–32 GB
- **Disk**: 2 x SSDs for storage, configured in RAID for redundancy
- **Network**: 1 Gbps minimum (10 Gbps preferred for higher throughput)

## 5. High Availability and Durability Configuration
- Implement a cluster with at least 3 brokers and 3 bookies for fault tolerance.
- Configure data replication (at least 3 replicas) to ensure durability.
- Use Pulsar's built-in mechanisms for load balancing and failover capabilities.

## 6. Monitoring and Performance Tuning Recommendations
- Use **Prometheus** and **Grafana** for monitoring metrics like message throughput, latency, and error rates.
- Enable Pulsar's built-in metrics collection by using the following settings in the configuration file:
  ```yaml
  metrics:
    enabled: true
  ```
- Regularly review and adjust the DistributedLog and Bookie configurations (e.g., `ledgerFlushThreshold`, `journalBufferSize`) to optimize performance.

## 7. Additional Considerations or Best Practices
- Regularly back up your important configurations and data.
- Review Pulsar's official documentation for updates and improvements: [Apache Pulsar Documentation](https://pulsar.apache.org/docs/en/)
- Consider security configurations such as TLS encryption for data in transit to protect data integrity and privacy.
- Test the Pulsar deployment with a load testing tool to simulate expected workloads before going live.

---
This setup provides a solid foundation for processing **50,000 messages per second** while ensuring high availability and durability of your Apache Pulsar system.