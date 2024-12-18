khushwant@khushwant:~$ cd Downloads/
khushwant@khushwant:~/Downloads$ ls
 ai-engineer.pdf                                                large_dataset.csv                               'Shopify CSV Sample.csv'
 anydesk_6.4.0-1_amd64.deb                                      postman-linux-x64.tar.gz                         spark-3.5.3-bin-hadoop3.tgz
 code_1.96.0-1733888194_amd64.deb                              'Resume-Khushwant- PythonDeveloper (1).docx'     'Strategy Trading Portal.pdf'
'Dotsquares Proposal Document for Trading Platfrom V1.0.docx'  'Resume-Khushwant- PythonDeveloper.docx'          thunderbird.tmp
 important_download                                            'Screencast from 16-12-24 05_42_49 PM IST.webm'   tws-latest-linux-x64.sh
 kafka-3.9.0-src.tgz                                           'Screencast from 16-12-24 06_19_45 PM IST.webm'
khushwant@khushwant:~/Downloads$ tar -xzf kafka-3.9.0-src.tgz
cd kafka-3.9.0-src
khushwant@khushwant:~/Downloads/kafka-3.9.0-src$ bin/zookeeper-server-start.sh config/zookeeper.properties
Classpath is empty. Please build the project first e.g. by running './gradlew jar -PscalaVersion=2.13.14'
khushwant@khushwant:~/Downloads/kafka-3.9.0-src$ ./gradlew jar
./gradlew: 119: curl: not found
./gradlew: 119: curl: not found
./gradlew: 119: curl: not found
Error: Could not find or load main class org.gradle.wrapper.GradleWrapperMain
Caused by: java.lang.ClassNotFoundException: org.gradle.wrapper.GradleWrapperMain
khushwant@khushwant:~/Downloads/kafka-3.9.0-src$ sudo apt update
sudo apt install curl -y
[sudo] password for khushwant: 
Get:1 https://packages.microsoft.com/repos/code stable InRelease [3,590 B]
Get:2 https://dl.google.com/linux/chrome/deb stable InRelease [1,825 B]                                                                         
Get:3 https://packages.microsoft.com/repos/code stable/main amd64 Packages [17.9 kB]                                                                 
Hit:4 http://in.archive.ubuntu.com/ubuntu jammy InRelease                                                                                
Get:5 http://security.ubuntu.com/ubuntu jammy-security InRelease [129 kB]                               
Get:6 http://in.archive.ubuntu.com/ubuntu jammy-updates InRelease [128 kB]                                                              
Get:7 https://dl.google.com/linux/chrome/deb stable/main amd64 Packages [1,224 B]                                                       
Hit:8 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease             

You can use '--warning-mode all' to show the individual deprecation warnings and determine if they come from your own scripts or plugins.

For more on this, please refer to https://docs.gradle.org/8.8/userguide/command_line_interface.html#sec:command_line_warnings in the Gradle documentation.

BUILD SUCCESSFUL in 4m 16s
156 actionable tasks: 156 executed
khushwant@khushwant:~/Downloads/kafka-3.9.0-src$ bin/zookeeper-server-start.sh config/zookeeper.properties
[2024-12-17 19:54:45,896] INFO Reading configuration from: config/zookeeper.properties (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2024-12-17 19:54:45,897] WARN config/zookeeper.properties is relative. Prepend ./ to indicate that you're sure! (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2024-12-17 19:54:45,899] INFO clientPortAddress is 0.0.0.0:2181 (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2024-12-17 19:54:45,899] INFO secureClientPort is not set (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2024-12-17 19:54:45,899] INFO observerMasterPort is not set (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2024-12-17 19:54:45,900] INFO metricsProvider.className is org.apache.zookeeper.metrics.impl.DefaultMetricsProvider (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2024-12-17 19:54:45,903] INFO Starting server (org.apache.zookeeper.server.ZooKeeperServerMain)
[2024-12-17 19:54:45,911] INFO ServerMetrics initialized with provider org.apache.zookeeper.metrics.impl.DefaultMetricsProvider@35e2d654 (org.apache.zookeeper.server.ServerMetrics)
[2024-12-17 19:54:45,912] INFO ACL digest algorithm is: SHA1 (org.apache.zookeeper.server.auth.DigestAuthenticationProvider)
[2024-12-17 19:54:45,912] INFO zookeeper.DigestAuthenticationProvider.enabled = true (org.apache.zookeeper.server.auth.DigestAuthenticationProvider)
[2024-12-17 19:54:45,914] INFO zookeeper.snapshot.trust.empty : false (org.apache.zookeeper.server.persistence.FileTxnSnapLog)
[2024-12-17 19:54:45,920] INFO  (org.apache.zookeeper.server.ZooKeeperServer)
[2024-12-17 19:54:45,921] INFO   ______                  _                                           (org.apache.zookeeper.server.ZooKeeperServer)
[2024-12-17 19:54:45,921] INFO  |___  /                 | |                                          (org.apache.zookeeper.server.ZooKeeperServer)
[2024-12-17 19:54:45,921] INFO     / /    ___     ___   | | __   ___    ___   _ __     ___   _ __    (org.apache.zookeeper.server.ZooKeeperServer)
[2024-12-17 19:54:45,921] INFO    / /    / _ \   / _ \  | |/ /  / _ \  / _ \ | '_ \   / _ \ | '__| (org.apache.zookeeper.server.ZooKeeperServer)
[2024-12-17 19:54:45,921] INFO   / /__  | (_) | | (_) | |   <  |  __/ |  __/ | |_) | |  __/ | |     (org.apache.zookeeper.server.ZooKeeperServer)
[2024-12-17 19:54:45,921] INFO  /_____|  \___/   \___/  |_|\_\  \___|  \___| | .__/   \___| |_| (org.apache.zookeeper.server.ZooKeeperServer)
[2024-12-17 19:54:45,921] INFO                                               | |                      (org.apache.zookeeper.server.ZooKeeperServer)
[2024-12-17 19:54:45,921] INFO                                               |_|                      (org.apache.zookeeper.server.ZooKeeperServer)
[2024-12-17 19:54:45,921] INFO  (org.apache.zookeeper.server.ZooKeeperServer)
[2024-12-17 19:54:45,922] INFO Server environment:zookeeper.version=3.8.4-9316c2a7a97e1666d8f4593f34dd6fc36ecc436c, built on 2024-02-12 22:16 UTC (org.apache.zookeeper.server.ZooKeeperServer)
[2024-12-17 19:54:45,922] INFO Server environment:host.name=khushwant (org.apache.zookeeper.server.ZooKeeperServer)
[2024-12-17 19:54:45,922] INFO Server environment:java.version=11.0.25 (org.ap




khushwant@khushwant:~/Downloads/kafka-3.9.0-src$ bin/kafka-server-start.sh config/server.properties
[2024-12-17 19:56:21,269] INFO Registered kafka:type=kafka.Log4jController MBean (kafka.utils.Log4jControllerRegistration$)
[2024-12-17 19:56:21,455] INFO Setting -D jdk.tls.rejectClientInitiatedRenegotiation=true to disable client-initiated TLS renegotiation (org.apache.zookeeper.common.X509Util)
[2024-12-17 19:56:21,546] INFO Registered signal handlers for TERM, INT, HUP (org.apache.kafka.common.utils.LoggingSignalHandler)
[2024-12-17 19:56:21,548] INFO starting (kafka.server.KafkaServer)
[2024-12-17 19:56:21,548] INFO Connecting to zookeeper on localhost:2181 (kafka.server.KafkaServer)
[2024-12-17 19:56:21,567] INFO [ZooKeeperClient Kafka server] Initializing a new session to localhost:2181. (kafka.zookeeper.ZooKeeperClient)
[2024-12-17 19:56:21,570] INFO Client environment:zookeeper.version=3.8.4-9316c2a7a97e1666d8f4593f34dd6fc36ecc436c, built on 2024-02-12 22:16 UTC (org.apache.zookeeper.ZooKeeper)
[2024-12-17 19:56:21,570] INFO Client environment:host.name=khushwant (org.apache.zookeeper.ZooKeeper)
[2024-12-17 19:56:21,570] INFO Client environment:java.version=11.0.25 (org.apache.zookeeper.ZooKeeper)
[2024-12-17 19:56:21,570] INFO Client environment:java.vendor=Ubuntu (org.apache.zookeeper.ZooKeeper)
[2024-12-17 19:56:21,570] INFO Client environment:java.home=/usr/lib/jvm/java-11-openjdk-amd64 (org.apache.zookeeper.ZooKeeper)



khushwant@khushwant:~/Downloads/kafka-3.9.0-src$ bin/kafka-topics.sh --list --bootstrap-server localhost:9092

khushwant@khushwant:~/Downloads/kafka-3.9.0-src$ 







khushwant@khushwant:~/Downloads/kafka-3.9.0-src$ bin/zookeeper-server-start.sh config/zookeeper.properties
[2024-12-17 20:02:29,236] INFO Reading configuration from: config/zookeeper.properties (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2024-12-17 20:02:29,237] WARN config/zookeeper.properties is relative. Prepend ./ to indicate that you're sure! (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2024-12-17 20:02:29,240] INFO clientPortAddress is 0.0.0.0:2181 (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2024-12-17 20:02:29,240] INFO secureClientPort is not set (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2024-12-17 20:02:29,240] INFO observerMasterPort is not set (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2024-12-17 20:02:29,240] INFO metricsProvider.className is org.apache.zookeeper.metrics.impl.DefaultMetricsProvider (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2024-12-17 20:02:29,241] INFO autopurge.snapRetainCount set to 3 (org.apache.zookeeper.server.DatadirCleanupManager)
[2024-12-17 20:02:29,241] INFO autopurge.purgeInterval set to 0 (org.apache.zookeeper.server.DatadirCleanupManager)
[2024-12-17 20:02:29,241] INFO Purge task is not scheduled. (org.apache.zookeeper.server.DatadirCleanupManager)
[2024-12-17 20:02:29,241] WARN Either no config or no quorum defined in config, running in standalone mode (org.apache.zookeeper.server.quorum.QuorumPeerMain)
[2024-12-17 20:02:29,242] INFO Log4j 1.2 jmx support not found; jmx disabled. (org.apache.zookeeper.jmx.ManagedUtil)
[2024-12-17 20:02:29,242] INFO Reading configuration from: config/zookeeper.properties (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2024-12-17 20:02:29,242] WARN config/zookeeper.properties is relative. Prepend ./ to indicate that you're sure! (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2024-12-17 20:02:29,243] INFO clientPortAddress is 0.0.0.0:2181 (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2024-12-17 20:02:29,243] INFO secureClientPort is not set (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2024-12-17 20:02:29,243] INFO observerMasterPort is not set (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2024-12-17 20:02:29,243] INFO metricsProvider.className is org.apache.zookeeper.metrics.impl.DefaultMetricsProvider (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2024-12-17 20:02:29,243] INFO Starting server (org.apache.zookeeper.server.ZooKeeperServerMain)
[2024-12-17 20:02:29,250] INFO ServerMetrics initialized with provider org.apache.zookeeper.metrics.impl.DefaultMetricsProvider@1bd4fdd (org.apache.zookeeper.server.ServerMetrics)
[2024-12-17 20:02:29,252] INFO ACL digest algorithm is: SHA1 (org.apache.zookeeper.server.auth.DigestAuthenticationProvider)
[2024-12-17 20:02:29,252] INFO zookeeper.DigestAuthenticationProvider.enabled = true (org.apache.zookeeper.server.auth.DigestAuthenticationProvider)
[2024-12-17 20:02:29,253] INFO zookeeper.snapshot.trust.empty : false (org.apache.zookeeper.server.persistence.FileTxnSnapLog)
[2024-12-17 20:02:29,259] INFO  (org.apache.zookeeper.server.ZooKeeperServer)
[2024-12-17 20:02:29,259] INFO   ______                  _                                           (org.apache.zookeeper.server.ZooKeeperServer)
[2024-12-17 20:02:29,259] INFO  |___  /                 | |                                          (org.apache.zookeeper.server.ZooKeeperServer)
[2024-12-17 20:02:29,259] INFO     / /    ___     ___   | | __   ___    ___   _ __     ___   _ __    (org.apache.zookeeper.server.ZooKeeperServer)
[2024-12-17 20:02:29,259] INFO    / /    / _ \   / _ \  | |/ /  / _ \  / _ \ | '_ \   / _ \ | '__| (org.apache.zookeeper.server.ZooKeeperServer)
[2024-12-17 20:02:29,259] INFO   / /__  | (_) | | (_) | |   <  |  __/ |  __/ | |_) | |  __/ | |     (org.apache.zookeeper.server.ZooKeeperServer)
[2024-12-17 20:02:29,260] INFO  /_____|  \___/   \___/  |_|\_\  \___|  \___| | .__/   \___| |_| (org.apache.zookeeper.server.ZooKeeperServer)
[2024-12-17 20:02:29,260] INFO                                               | |                      (org.apache.zookeeper.server.ZooKeeperServer)
[2024-12-17 20:02:29,260] INFO                                               |_|                      (org.apache.zookeeper.server.ZooKeeperServer)
[2024-12-17 20:02:29,260] INFO  (org.apache.zookeeper.server.ZooKeeperServer)
[2024-12-17 20:02:29,260] INFO Server environment:zookeeper.version=3.8.4-9316c2a7a97e1666d8f4593f34dd6fc36ecc436c, built on 2024-02-12 22:16 UTC (org.apache.zookeeper.server.ZooKeeperServer)
[2024-12-17 20:02:29,261] INFO Server environment:host.name=khushwant (org.apache.zookeeper.server.ZooKeeperServer)
[2024-12-17 20:02:29,261] INFO Server environment:java.version=11.0.25 (org.apache.zookeeper.server.ZooKeeperServer)
[2024-12-17 20:02:29,261] INFO Server environment:java.vendor=Ubuntu (org.apache.zookeeper.server.ZooKeeperServer)



[2024-12-17 20:02:29,267] INFO zookeeper.enforce.auth.schemes = [] (org.apache.zookeeper.server.AuthenticationHelper)
[2024-12-17 20:02:29,267] INFO Created server with tickTime 3000 ms minSessionTimeout 6000 ms maxSessionTimeout 60000 ms clientPortListenBacklog -1 datadir /tmp/zookeeper/version-2 snapdir /tmp/zookeeper/version-2 (org.apache.zookeeper.server.ZooKeeperServer)
[2024-12-17 20:02:29,271] INFO Using org.apache.zookeeper.server.NIOServerCnxnFactory as server connection factory (org.apache.zookeeper.server.ServerCnxnFactory)
[2024-12-17 20:02:29,271] WARN maxCnxns is not configured, using default value 0. (org.apache.zookeeper.server.ServerCnxnFactory)
[2024-12-17 20:02:29,272] INFO Configuring NIO connection handler with 10s sessionless connection timeout, 2 selector thread(s), 24 worker threads, and 64 kB direct buffers. (org.apache.zookeeper.server.NIOServerCnxnFactory)
[2024-12-17 20:02:29,276] INFO binding to port 0.0.0.0/0.0.0.0:2181 (org.apache.zookeeper.server.NIOServerCnxnFactory)
[2024-12-17 20:02:29,277] ERROR Unexpected exception, exiting abnormally (org.apache.zookeeper.server.ZooKeeperServerMain)
java.net.BindException: Address already in use
	at java.base/sun.nio.ch.Net.bind0(Native Method)
	at java.base/sun.nio.ch.Net.bind(Net.java:459)
	at java.base/sun.nio.ch.Net.bind(Net.java:448)
	at java.base/sun.nio.ch.ServerSocketChannelImpl.bind(ServerSocketChannelImpl.java:227)
	at java.base/sun.nio.ch.ServerSocketAdaptor.bind(ServerSocketAdaptor.java:80)
	at java.base/sun.nio.ch.ServerSocketAdaptor.bind(ServerSocketAdaptor.java:73)
	at org.apache.zookeeper.server.NIOServerCnxnFactory.configure(NIOServerCnxnFactory.java:662)
	at org.apache.zookeeper.server.ZooKeeperServerMain.runFromConfig(ZooKeeperServerMain.java:160)
	at org.apache.zookeeper.server.ZooKeeperServerMain.initializeAndRun(ZooKeeperServerMain.java:113)
	at org.apache.zookeeper.server.ZooKeeperServerMain.main(ZooKeeperServerMain.java:68)
	at org.apache.zookeeper.server.quorum.QuorumPeerMain.initializeAndRun(QuorumPeerMain.java:141)
	at org.apache.zookeeper.server.quorum.QuorumPeerMain.main(QuorumPeerMain.java:91)
[2024-12-17 20:02:29,278] INFO ZooKeeper audit is disabled. (org.apache.zookeeper.audit.ZKAuditProvider)
[2024-12-17 20:02:29,279] ERROR Exiting JVM with code 1 (org.apache.zookeeper.util.ServiceUtils)
khushwant@khushwant:~/Downloads/kafka-3.9.0-src$ bin/kafka-topics.sh --create --topic test-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
Created topic test-topic.
khushwant@khushwant:~/Downloads/kafka-3.9.0-src$ bin/kafka-topics.sh --create --topic file-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
Created topic file-topic.
khushwant@khushwant:~/Downloads/kafka-3.9.0-src$ 

