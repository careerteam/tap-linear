from singer_sdk import typing as th

issuesSchema = th.PropertiesList(
    th.Property("id", th.StringType),
    th.Property("title", th.StringType),
    th.Property("description", th.StringType),
    th.Property("url", th.StringType),
    th.Property("updatedAt", th.DateTimeType),
    th.Property("archivedAt", th.DateTimeType),
    th.Property("autoArchivedAt", th.DateTimeType),
    th.Property("autoClosedAt", th.DateTimeType),
    th.Property("canceledAt", th.DateTimeType),
    th.Property("completedAt", th.DateTimeType),
    th.Property("createdAt", th.DateTimeType),
    th.Property("startedAt", th.DateTimeType),
    th.Property("startedTriageAt", th.DateTimeType),
    th.Property("triagedAt", th.DateTimeType),

    th.Property("estimate", th.StringType),
    th.Property("priority", th.StringType),
    th.Property("priorityLabel", th.StringType),
    th.Property("dueDate", th.DateType),

    th.Property(
        "creator",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
            th.Property("email", th.StringType),
        ),
    ),
    th.Property(
        "assignee",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
            th.Property("email", th.StringType),
        ),
    ),
    th.Property(
        "project",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
        ),
    ),
    th.Property(
        "team",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
        ),
    ),
).to_dict()
