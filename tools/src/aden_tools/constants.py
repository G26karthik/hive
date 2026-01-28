"""
Constants for aden_tools package.

Centralizes default values and configuration constants for tools.
"""

# ============================================================================
# Command Execution
# ============================================================================

# Default timeout for command execution (seconds)
DEFAULT_COMMAND_TIMEOUT_SECONDS = 60

# ============================================================================
# File System Operations
# ============================================================================

# Maximum file size for reading (bytes) - 10MB
MAX_FILE_READ_SIZE = 10 * 1024 * 1024

# Default chunk size for file reading
DEFAULT_READ_CHUNK_SIZE = 8192

# ============================================================================
# Web Operations
# ============================================================================

# Default timeout for web requests (seconds)
DEFAULT_WEB_REQUEST_TIMEOUT = 30

# Maximum page size for web scraping (bytes) - 5MB
MAX_WEB_PAGE_SIZE = 5 * 1024 * 1024
