import sentry_sdk


def sentry_config()-> bool:
    sentry_sdk.init(
        dsn="https://e0ef8b32cac7d5e8ff89b98e00211dd0@o4508304884301824.ingest.us.sentry.io/4508304902062080",
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for tracing.
        traces_sample_rate=1.0,
        _experiments={
            # Set continuous_profiling_auto_start to True
            # to automatically start the profiler on when
            # possible.
            "continuous_profiling_auto_start": True,
        },
    )

    return True
