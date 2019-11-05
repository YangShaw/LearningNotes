
# SkyWalking learning


## 介绍
- 应用性能监控系统（APM），功能是对于分布式云原生架构的monitoring,tracing,diagnosing诊断.可以收集，分析，整合，可视化数据。
    - cloud native architecture: 应用容器化，面向微服务架构，应用支持容器的编排调度。代表技术包括容器，微服务，服务网格，不可变基础设施和声明式API。优点是：构建容错性好，易于管理，便于观察的松耦合系统。便于管控。
- 特性：
    - Service, service instance, endpoint metrics analysis
    - Root cause analysis
    - Service topology map analysis
    - Service, service instance and endpoint dependency analysis
    - Slow services and endpoints detected
    - Performance optimization
    - Distributed tracing and context propagation传播
    - Database access metrics. Detect slow database access statements(including SQL statements).
    - Alarm

- 收集来自多种source和format的telemetry data；

- 架构
    - probes：不同的源有不同的版本；收集数据，并格式化；
    - platform backend: 
