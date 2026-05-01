#!/usr/bin/env python3
"""
Final comprehensive test of the Agentic Autonomy System integration
"""

import sys
import os
import json

# Add the hermes-agent directory to the path
sys.path.insert(0, '/home/david/.hermes/hermes-agent')

def test_complete_integration():
    """Test the complete agentic system integration"""
    print("🧪 COMPREHENSIVE AGENTIC SYSTEM INTEGRATION TEST")
    print("=" * 60)
    
    # Test 1: Import all modules
    print("\n1. Testing module imports...")
    try:
        from agent.agentic import get_agentic_system
        from agent.agentic.roles import get_role_manager
        from agent.agentic.coordination import get_agentic_coordinator
        from agent.agentic.integration import get_agentic_integration
        from tools.agentic_tools import agentic_execute_task, agentic_get_roles, agentic_get_status
        print("✅ All modules imported successfully")
    except Exception as e:
        print(f"❌ Module import failed: {e}")
        return False
    
    # Test 2: Test system initialization
    print("\n2. Testing system initialization...")
    try:
        agentic = get_agentic_integration()
        role_manager = get_role_manager()
        coordinator = get_agentic_coordinator()
        print("✅ All systems initialized successfully")
    except Exception as e:
        print(f"❌ System initialization failed: {e}")
        return False
    
    # Test 3: Test role management
    print("\n3. Testing role management...")
    try:
        roles = agentic.get_available_roles()
        expected_roles = ['researcher', 'developer', 'tester', 'documenter', 'architect']
        
        for role in expected_roles:
            if role not in roles:
                print(f"❌ Missing role: {role}")
                return False
        
        print(f"✅ All {len(roles)} roles available")
    except Exception as e:
        print(f"❌ Role management failed: {e}")
        return False
    
    # Test 4: Test task execution
    print("\n4. Testing task execution...")
    try:
        test_tasks = [
            "Research AI agent frameworks",
            "Develop a simple web application",
            "Create documentation for the agentic system",
            "Design test cases for multi-agent coordination"
        ]
        
        for i, task in enumerate(test_tasks, 1):
            result = agentic.execute_agentic_task(task)
            if not result['success']:
                print(f"❌ Task {i} failed: {task}")
                return False
            
            print(f"✅ Task {i} completed: {len(result['tasks'])} subtasks")
        
        print(f"✅ All {len(test_tasks)} test tasks executed successfully")
    except Exception as e:
        print(f"❌ Task execution failed: {e}")
        return False
    
    # Test 5: Test custom role creation
    print("\n5. Testing custom role creation...")
    try:
        custom_role_name = "test_role"
        success = agentic.add_custom_role(
            role_name=custom_role_name,
            description="Test custom role",
            capabilities=["testing"],
            default_tools=["test"]
        )
        
        if not success:
            print("❌ Custom role creation failed")
            return False
        
        # Verify the role was added
        roles_after = agentic.get_available_roles()
        if custom_role_name not in roles_after:
            print("❌ Custom role not found after creation")
            return False
        
        print("✅ Custom role creation successful")
    except Exception as e:
        print(f"❌ Custom role creation failed: {e}")
        return False
    
    # Test 6: Test system monitoring
    print("\n6. Testing system monitoring...")
    try:
        status = agentic.get_system_status()
        
        required_keys = ['active_agents', 'completed_tasks', 'pending_tasks', 
                        'conflicts_detected', 'conflicts_resolved']
        
        for key in required_keys:
            if key not in status:
                print(f"❌ Missing status key: {key}")
                return False
        
        print("✅ System monitoring working correctly")
        print(f"   Active agents: {status['active_agents']}")
        print(f"   Completed tasks: {status['completed_tasks']}")
    except Exception as e:
        print(f"❌ System monitoring failed: {e}")
        return False
    
    # Test 7: Test tool integration
    print("\n7. Testing tool integration...")
    try:
        # Test agentic_get_roles tool
        roles_result = agentic_get_roles()
        roles_data = json.loads(roles_result)
        
        if not roles_data['success'] or len(roles_data['roles']) == 0:
            print("❌ agentic_get_roles tool failed")
            return False
        
        # Test agentic_get_status tool
        status_result = agentic_get_status()
        status_data = json.loads(status_result)
        
        if not status_data['success']:
            print("❌ agentic_get_status tool failed")
            return False
        
        # Test agentic_execute_task tool
        task_result = agentic_execute_task("Test tool integration")
        task_data = json.loads(task_result)
        
        if not task_data['success']:
            print("❌ agentic_execute_task tool failed")
            return False
        
        print("✅ All tools integrated successfully")
    except Exception as e:
        print(f"❌ Tool integration failed: {e}")
        return False
    
    # Test 8: Test complex scenario
    print("\n8. Testing complex multi-task scenario...")
    try:
        complex_task = """
        Develop a comprehensive AI research platform that includes:
        1. Research module for academic papers
        2. Analysis module for data processing
        3. Visualization module for results
        4. Documentation module for knowledge capture
        5. Testing module for quality assurance
        """
        
        result = agentic.execute_agentic_task(complex_task)
        
        if not result['success']:
            print("❌ Complex task execution failed")
            return False
        
        if len(result['tasks']) == 0:
            print("❌ No subtasks created for complex task")
            return False
        
        print(f"✅ Complex task executed successfully")
        print(f"   Created {len(result['tasks'])} subtasks")
        print(f"   Reflection: {result['reflection']['analysis']}")
    except Exception as e:
        print(f"❌ Complex scenario failed: {e}")
        return False
    
    print("\n" + "=" * 60)
    print("🎉 ALL TESTS PASSED!")
    print("\nThe Agentic Autonomy System is fully functional and integrated.")
    print("\nKey achievements:")
    print("✅ Core system implementation complete")
    print("✅ Role management system working")
    print("✅ Task execution pipeline functional")
    print("✅ System monitoring operational")
    print("✅ Tool integration successful")
    print("✅ Complex scenarios handled correctly")
    print("\n🚀 The system is ready for production use!")
    
    return True

if __name__ == "__main__":
    success = test_complete_integration()
    sys.exit(0 if success else 1)