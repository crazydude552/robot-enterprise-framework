class EnvInitializer:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def initialize_suite_environment(self, env_name, api_url, timeout, header_type="FIN"):
        """Prints environment details and validates required startup configuration variables."""
        print(f"==================================================")
        print(f" Starting Suite Execution on Target Env: {env_name}")
        print(f" API Endpoint: {api_url}")
        print(f" Execution Timeout: {timeout} seconds")
        print(f" Header Context Loaded: {header_type}")
        print(f"==================================================")

        if not api_url or not env_name:
            raise ValueError("Environment configuration incomplete: Missing API_URL or ENV_NAME")

        return True

    def combine_headers_and_data(self, default_headers, test_data_dict):
        """Merges default headers with specific test case parameters."""
        combined = {**default_headers, **test_data_dict}
        return combined