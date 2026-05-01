#!/usr/bin/env python3
"""
Simple Agentic System Test Runner

Run tests without pytest configuration conflicts.
"""

import sys
import os
import unittest
import time

# Add the hermes-agent directory to the path
sys.path.insert(0, '/home/david/.hermes/hermes-agent')

# Import agentic components
from agent.agentic.integration import get_agentic_integration
from agent.agentic import get_agentic_system
from agent.agentic.roles import get_role_manager
from agent.agentic.coordination import get_agentic_coordinator

class TestAgenticSystem(unittest.TestCase):
    """Test cases for the agentic system"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.agentic = get_agentic_integration()
        self.system = get_agentic_system()
        self.roles = get_role_manager()
        self.coordinator = get_agentic_coordinator()
    
    def test_system_initialization(self):
        """Test that all systems initialize correctly"""
        self.assertIsNotNone(self.agentic)
        self.assertIsNotNone(self.system)
        self.assertIsNotNone(self.roles)
        self.assertIsNotNone(self.coordinator)
    
    def test_role_management(self):
        """Test role management functionality"""
        # Test built-in roles
        available_roles = self.agentic.get_available_roles()
        self.assertGreaterEqual(len(available_roles), 5)
        
        # Test custom role creation
        success = self.agentic.add_custom_role(
            role_name="test_role",
            description="Test role",
            capabilities=["testing"],
            default_tools=["test"]
        )
        self.assertTrue(success)
    
    def test_task_execution(self):
        """Test task execution functionality"""
        result = self.agentic.execute_agentic_task("Test task execution")
        self.assertTrue(result["success"])
        self.assertGreater(len(result["tasks"]), 0)
    
    def test_system_status(self):
        """Test system status monitoring"""
        status = self.agentic.get_system_status()
        self.assertIn("active_agents", status)
        self.assertIn("completed_tasks", status)
        self.assertIn("pending_tasks", status)
    
    def test_task_decomposition(self):
        """Test task decomposition"""
        tasks = self.system.planner.decompose_task("Research AI frameworks")
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].description, "Research AI frameworks")
    
    def test_coordination(self):
        """Test multi-agent coordination"""
        # Add test tasks
        self.coordinator.add_task("test_task_1")
        self.coordinator.add_task("test_task_2")
        
        # Verify tasks were added
        self.assertEqual(len(self.coordinator.task_queue), 2)
        
        # Complete tasks
        self.coordinator.complete_task("test_task_1")
        self.coordinator.complete_task("test_task_2")
        
        # Verify completion
        self.assertEqual(len(self.coordinator.task_queue), 0)
        self.assertEqual(self.coordinator.state.completed_tasks, 2)

def run_tests():
    """Run all agentic system tests"""
    print("🧪 Running Agentic System Tests...")
    print("=" * 60)
    
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAgenticSystem)
    
    # Create test runner
    runner = unittest.TextTestRunner(verbosity=2)
    
    # Run tests
    result = runner.run(suite)
    
    print("\n" + "=" * 60)
    if result.wasSuccessful():
        print("🎉 All tests passed!")
        return True
    else:
        print("❌ Some tests failed!")
        return False

def run_debug_session():
    """Run interactive debug session"""
    print("🐛 Agentic System Debug Session")
    print("=" * 60)
    
    try:
        agentic = get_agentic_integration()
        
        while True:
            print("\nOptions:")
            print("1. Execute task")
            print("2. Show status")
            print("3. List roles")
            print("4. Exit")
            
            choice = input("\nChoose option (1-4): ").strip()
            
            if choice == '1':
                task = input("Enter task: ")
                result = agentic.execute_agentic_task(task)
                print(f"Result: {result}")
                
            elif choice == '2':
                status = agentic.get_system_status()
                for key, value in status.items():
                    print(f"{key}: {value}")
                
            elif choice == '3':
                roles = agentic.get_available_roles()
                for role_name in roles.keys():
                    print(f"- {role_name}")
                
            elif choice == '4':
                break
                
            else:
                print("Invalid choice")
                
    except Exception as e:
        print(f"Error: {e}")
        return False
    
    return True

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Agentic System Test Runner")
    parser.add_argument('--debug', action='store_true', help="Start debug session")
    args = parser.parse_args()
    
    if args.debug:
        return run_debug_session()
    else:
        return run_tests()

if __name__ == '__main__':
    import argparse
    success = main()
    sys.exit(0 if success else 1)