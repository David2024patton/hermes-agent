#!/usr/bin/env python3
"""
Agentic System Test Runner

This script provides a standalone way to test the agentic system
without requiring the full Hermes Agent infrastructure.
"""

import sys
import os
import argparse
import pytest

# Add the hermes-agent directory to the path
sys.path.insert(0, '/home/david/.hermes/hermes-agent')

def run_agentic_tests():
    """Run the agentic system tests"""
    print("🧪 Running Agentic System Tests...")
    print("=" * 50)
    
    # Run pytest on the agentic test module
    exit_code = pytest.main([
        'tests/test_agentic_system.py',
        '-v',
        '--tb=short'
    ])
    
    return exit_code == 0

def run_debug_session():
    """Run an interactive debug session for the agentic system"""
    print("🐛 Starting Agentic System Debug Session...")
    print("=" * 50)
    
    try:
        # Import agentic components
        from agent.agentic.integration import get_agentic_integration
        from agent.agentic import get_agentic_system
        from agent.agentic.roles import get_role_manager
        from agent.agentic.coordination import get_agentic_coordinator
        
        # Initialize systems
        agentic = get_agentic_integration()
        system = get_agentic_system()
        roles = get_role_manager()
        coordinator = get_agentic_coordinator()
        
        print("✅ All agentic systems initialized")
        print("\nAvailable systems:")
        print("  - agentic: Main integration layer")
        print("  - system: Core agentic system")
        print("  - roles: Role management system")
        print("  - coordinator: Multi-agent coordinator")
        
        # Start interactive session
        while True:
            print("\n" + "-" * 50)
            print("Debug Menu:")
            print("1. Execute test task")
            print("2. Show system status")
            print("3. List available roles")
            print("4. Add custom role")
            print("5. Test task decomposition")
            print("6. Test coordination")
            print("7. Exit")
            
            choice = input("\nEnter your choice (1-7): ").strip()
            
            if choice == '1':
                task = input("Enter task description: ")
                result = agentic.execute_agentic_task(task)
                print(f"\nResult: {result}")
                
            elif choice == '2':
                status = agentic.get_system_status()
                print(f"\nSystem Status:")
                for key, value in status.items():
                    print(f"  {key}: {value}")
                
            elif choice == '3':
                available_roles = agentic.get_available_roles()
                print(f"\nAvailable Roles:")
                for role_name, role_info in available_roles.items():
                    print(f"  - {role_name}: {role_info['description']}")
                
            elif choice == '4':
                role_name = input("Enter role name: ")
                description = input("Enter description: ")
                capabilities = input("Enter capabilities (comma-separated): ").split(',')
                default_tools = input("Enter default tools (comma-separated): ").split(',')
                
                success = agentic.add_custom_role(
                    role_name=role_name.strip(),
                    description=description.strip(),
                    capabilities=[c.strip() for c in capabilities],
                    default_tools=[t.strip() for t in default_tools]
                )
                
                if success:
                    print(f"✅ Role '{role_name}' added successfully")
                else:
                    print(f"❌ Failed to add role '{role_name}'")
                
            elif choice == '5':
                task_desc = input("Enter task to decompose: ")
                tasks = system.planner.decompose_task(task_desc)
                print(f"\nDecomposed into {len(tasks)} task(s):")
                for task in tasks:
                    print(f"  - {task.task_id[:8]}: {task.description}")
                
            elif choice == '6':
                # Test coordination
                coordinator.add_task("test_task_1")
                coordinator.add_task("test_task_2")
                
                status = coordinator.get_system_status()
                print(f"\nCoordinator Status:")
                print(f"  Pending tasks: {status['pending_tasks']}")
                print(f"  Task queue: {coordinator.task_queue}")
                
                # Clean up
                coordinator.complete_task("test_task_1")
                coordinator.complete_task("test_task_2")
                
            elif choice == '7':
                print("👋 Exiting debug session...")
                break
                
            else:
                print("❌ Invalid choice. Please try again.")
                
    except Exception as e:
        print(f"❌ Error in debug session: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

def run_benchmark():
    """Run performance benchmarks for the agentic system"""
    print("⏱️  Running Agentic System Benchmarks...")
    print("=" * 50)
    
    try:
        import time
        from agent.agentic.integration import get_agentic_integration
        
        agentic = get_agentic_integration()
        
        # Benchmark 1: Task execution speed
        print("\n📊 Benchmark 1: Task Execution Speed")
        start_time = time.time()
        
        for i in range(10):
            agentic.execute_agentic_task(f"Benchmark task {i}")
        
        end_time = time.time()
        avg_time = (end_time - start_time) / 10
        
        print(f"  Executed 10 tasks in {end_time - start_time:.3f} seconds")
        print(f"  Average time per task: {avg_time:.3f} seconds")
        
        # Benchmark 2: Role management
        print("\n📊 Benchmark 2: Role Management")
        start_time = time.time()
        
        for i in range(5):
            agentic.add_custom_role(
                role_name=f"benchmark_role_{i}",
                description=f"Benchmark role {i}",
                capabilities=[f"capability_{i}"],
                default_tools=[f"tool_{i}"]
            )
        
        end_time = time.time()
        roles = agentic.get_available_roles()
        
        print(f"  Added 5 custom roles in {end_time - start_time:.3f} seconds")
        print(f"  Total roles: {len(roles)}")
        
        # Benchmark 3: System status
        print("\n📊 Benchmark 3: System Status Monitoring")
        start_time = time.time()
        
        for i in range(100):
            status = agentic.get_system_status()
        
        end_time = time.time()
        
        print(f"  Retrieved system status 100 times in {end_time - start_time:.3f} seconds")
        print(f"  Average time per status check: {(end_time - start_time)/100:.3f} seconds")
        
        print("\n✅ Benchmarks completed successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Benchmark failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def run_integration_test():
    """Run integration tests with the Hermes Agent tool system"""
    print("🔌 Running Agentic Integration Tests...")
    print("=" * 50)
    
    try:
        from tools.agentic_tools import (
            agentic_execute_task,
            agentic_get_roles,
            agentic_get_status,
            register_agentic_tools,
            TOOL_SCHEMAS
        )
        from tools.registry import registry
        import json
        
        # Register tools
        register_agentic_tools(registry)
        print("✅ Agentic tools registered with Hermes Agent")
        
        # Test tool schemas
        print(f"\n📋 Registered Tool Schemas:")
        for schema in TOOL_SCHEMAS:
            print(f"  - {schema['name']}")
        
        # Test tool execution
        print("\n🧪 Testing Tool Execution:")
        
        # Test agentic_get_roles
        roles_result = agentic_get_roles()
        roles_data = json.loads(roles_result)
        print(f"  ✅ agentic_get_roles: {len(roles_data['roles'])} roles found")
        
        # Test agentic_get_status
        status_result = agentic_get_status()
        status_data = json.loads(status_result)
        print(f"  ✅ agentic_get_status: {status_data['status']['active_agents']} active agents")
        
        # Test agentic_execute_task
        task_result = agentic_execute_task("Integration test task")
        task_data = json.loads(task_result)
        print(f"  ✅ agentic_execute_task: {len(task_data['result']['tasks'])} tasks created")
        
        print("\n✅ All integration tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ Integration test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main entry point for the agentic test runner"""
    parser = argparse.ArgumentParser(
        description="Agentic System Test Runner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python test_agentic_runner.py tests          # Run all agentic tests
  python test_agentic_runner.py debug           # Start interactive debug session
  python test_agentic_runner.py benchmark        # Run performance benchmarks
  python test_agentic_runner.py integration     # Test Hermes integration
        """)
    
    parser.add_argument(
        'command',
        choices=['tests', 'debug', 'benchmark', 'integration'],
        help='Command to run'
    )
    
    args = parser.parse_args()
    
    if args.command == 'tests':
        success = run_agentic_tests()
    elif args.command == 'debug':
        success = run_debug_session()
    elif args.command == 'benchmark':
        success = run_benchmark()
    elif args.command == 'integration':
        success = run_integration_test()
    
    return 0 if success else 1

if __name__ == '__main__':
    sys.exit(main())