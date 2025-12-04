issuesQuery = """
query Issues($next: String, $replicationKeyValue: DateTimeOrDuration) {
    issues(
        first: 100
        after: $next
        filter: { updatedAt: {gt: $replicationKeyValue } }
    ) {
        pageInfo {
            hasNextPage
            endCursor
        }
        nodes {
            id
            title
            description
            url

            updatedAt
            archivedAt
            autoArchivedAt
            autoClosedAt
            canceledAt
            completedAt
            createdAt
            startedAt
            startedTriageAt
            triagedAt

            estimate
            priority
            priorityLabel
            dueDate

            creator {
                id
                name
                email
            }
            assignee {
                id
                name
                email
            }

            project {
                id
                name
            }
            team {
                id
                name
            }
        }
    }
}
"""
