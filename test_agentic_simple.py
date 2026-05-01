#!/usr/bin/env python3
"""
Test the agentic tools integration with Hermes Agent
"""

import sys
import os

# Add the hermes-agent directory to the path
sys.path.insert(0, '/home/david/.hermes/hermes-agent')

# Import the agentic tools directly
from tools.agentic_tools import agentic_get_roles, agentic_get_status, agentic_execute_task
import json

def test_agentic_tools_integration():
    """Test that agentic tools work correctly"""
    print("Testing Agentic Tools Integration...")
    print("=" * 50)
    
    # Test 1: Test agentic_get_roles
    print("\n1. Testing agentic_get_roles...")
    try:
        roles_result = agentic_get_roles()
        roles_data = json.loads(roles_result)
        print("✓ agentic_get_roles executed successfully")
        print(f"  Roles found: {len(roles_data['roles'])}")
        print(f"  Available roles: {list(roles_data['roles'].keys())}")
    except Exception as e:
        print(f"✗ agentic_get_roles failed: {e}")
        return False
    
    # Test 2: Test agentic_get_status
    print("\n2. Testing agentic_get_status...")
    try:
        status_result = agentic_get_status()
        status_data = json.loads(status_result)
        print("✓ agentic_get_status executed successfully")
        print(f"  Active agents: {status_data['status']['active_agents']}")
        print(f"  Completed tasks: {status_data['status']['completed_tasks']}")
    except Exception as e:
        print(f"✗ agentic_get_status failed: {e}")
        return False
    
    # Test 3: Test agentic_execute_task
    print("\n3. Testing agentic_execute_task...")
    try:
        task_result = agentic_execute_task("Research AI agent frameworks and summarize findings")
        task_data = json.loads(task_result)
        print("✓ agentic_execute_task executed successfully")
        print(f"  Task success: {task_data['success']}")
        print(f"  Tasks created: {len(task_data['result']['tasks'])}")
        print(f"  Reflection: {task_data['result']['reflection']['analysis']}")
    except Exception as e:
        print(f"✗ agentic_execute_task failed: {e}")
        return False
    
    print("\n" + "=" * 50)
    print("All agentic tools integration tests passed!")
    return True

if __name__ == "__main__":
    success = test_agentic_tools_integration()
    sys.exit(0 if success else 1)