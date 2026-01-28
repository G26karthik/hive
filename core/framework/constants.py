"""
Framework-wide constants and default values.

This module centralizes magic numbers and default configuration values
used throughout the framework to improve maintainability and consistency.
"""

# ============================================================================
# Graph Execution Limits
# ============================================================================

# Maximum number of steps a graph can execute before being terminated
DEFAULT_MAX_GRAPH_STEPS = 100

# Maximum number of retries per node when execution fails
DEFAULT_MAX_RETRIES_PER_NODE = 3

# Default timeout for parallel branch execution (seconds)
DEFAULT_PARALLEL_BRANCH_TIMEOUT_SECONDS = 300.0

# ============================================================================
# LLM Configuration
# ============================================================================

# Default model for Anthropic provider
DEFAULT_ANTHROPIC_MODEL = "claude-haiku-4-5-20251001"

# Default max tokens for LLM completions
DEFAULT_MAX_TOKENS = 1024

# Max tokens for fast model cleansing operations
DEFAULT_CLEANSING_MAX_TOKENS = 500

# Default max retries for output cleansing
DEFAULT_CLEANSING_MAX_RETRIES = 2

# ============================================================================
# CLI Output Formatting
# ============================================================================

# Width of separator lines in CLI output
CLI_SEPARATOR_WIDTH = 60

# Maximum characters to display for large outputs
CLI_OUTPUT_TRUNCATE_SHORT = 200
CLI_OUTPUT_TRUNCATE_MEDIUM = 300
CLI_OUTPUT_TRUNCATE_LONG = 500
CLI_OUTPUT_TRUNCATE_APPROVAL = 2000

# Maximum characters for description previews
CLI_DESCRIPTION_PREVIEW_LENGTH = 60

# ============================================================================
# Code Sandbox
# ============================================================================

# Default timeout for code execution in sandbox (seconds)
DEFAULT_SANDBOX_TIMEOUT_SECONDS = 5

# Default timeout for command execution (seconds)
DEFAULT_COMMAND_TIMEOUT_SECONDS = 60

# ============================================================================
# Memory and Caching
# ============================================================================

# Maximum size for JSON extraction to prevent performance issues
MAX_JSON_EXTRACTION_SIZE = 1024 * 1024  # 1MB

# ============================================================================
# Error Handling
# ============================================================================

# Default strategies for parallel execution failures
PARALLEL_FAILURE_STRATEGIES = ["fail_all", "continue_others", "wait_all"]

# Default strategies for memory conflict resolution
MEMORY_CONFLICT_STRATEGIES = ["last_wins", "first_wins", "error"]
