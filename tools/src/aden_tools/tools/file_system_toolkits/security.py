import os

# Use user home directory for workspaces
WORKSPACES_DIR = os.path.expanduser("~/.hive/workdir/workspaces")

# Invalid characters that indicate path traversal attempts
INVALID_ID_CHARS = {"..", "/", "\\", "\x00"}


def get_secure_path(path: str, workspace_id: str, agent_id: str, session_id: str) -> str:
    """Resolve and verify a path within a 3-layer sandbox (workspace/agent/session).
    
    Security improvements:
    - Validates ID parameters to prevent injection attacks
    - Uses realpath() to resolve symlinks and prevent symlink-based traversal
    - Strict boundary checking to ensure paths stay within sandbox
    
    Args:
        path: File path to resolve (relative to session root)
        workspace_id: Workspace identifier
        agent_id: Agent identifier  
        session_id: Session identifier
        
    Returns:
        Secure absolute path within the sandbox
        
    Raises:
        ValueError: If parameters are invalid or path escapes sandbox
    """
    # Validate required parameters
    if not workspace_id or not agent_id or not session_id:
        raise ValueError("workspace_id, agent_id, and session_id are all required")
    
    # Check for path traversal attempts in IDs
    for param_name, param_value in [
        ("workspace_id", workspace_id),
        ("agent_id", agent_id), 
        ("session_id", session_id)
    ]:
        if not param_value.strip():
            raise ValueError(f"{param_name} cannot be empty or whitespace")
        for invalid_char in INVALID_ID_CHARS:
            if invalid_char in param_value:
                raise ValueError(
                    f"{param_name} contains invalid characters. "
                    f"Path traversal attempts are not allowed."
                )

    # Ensure session directory exists: runtime/workspace_id/agent_id/session_id
    session_dir = os.path.join(WORKSPACES_DIR, workspace_id, agent_id, session_id)
    os.makedirs(session_dir, exist_ok=True)

    # Resolve absolute path
    if os.path.isabs(path):
        # Treat absolute paths as relative to the session root if they start with /
        rel_path = path.lstrip(os.sep)
        final_path = os.path.abspath(os.path.join(session_dir, rel_path))
    else:
        final_path = os.path.abspath(os.path.join(session_dir, path))

    # Resolve symlinks to prevent symlink-based path traversal
    final_path_real = os.path.realpath(final_path)
    session_dir_real = os.path.realpath(session_dir)
    
    # Verify path is within session_dir (must start with session_dir + separator, or be exact match)
    if not (final_path_real.startswith(session_dir_real + os.sep) or final_path_real == session_dir_real):
        raise ValueError(f"Access denied: Path '{path}' is outside the session sandbox.")

    return final_path
