# Alert_system-ver_2

We present a more advanced (compared to previously posted here) notification system for our application. Statistical methods were used to detect anomalies. We used ***Aeroflow*** as an orchestrator.
The system checks the following key metrics every 15 minutes:
- number of active users (news feed) (in general; in the context of 'source' ; in the context of 'os');
- number of views (news feed) (in general; in the context of 'source' ; in the context of 'os');
- number of likes (news feed) (in general; in the context of 'source' ; in the context of 'os');
- CTR (news feed) (in general; in the context of 'source' ; in the context of 'os ' );
- number of views per user (news feed) (in general; in the context of 'source' ; in the context of 'os');
- number of likes per user (news feed) (in general; in the context of 'source' ; in the context of 'os');
- number of active users (messenger) (in general; in the context of 'source' ; in the context of 'os');
- number of sent messages (messenger) (in general; in the context of 'source' ; in the context of 'os');
- number of messages per user (messenger) (in general; in the context of 'source' ; in the context of 'os ').

When an abnormal value is detected, an alert is sent to the Telegram chat — a message with the following information: metric, its value, deviation value.
The message contains additional information that will help in studying the causes of the anomaly - a link to the dashboard (prepared in the ***Superset***).
