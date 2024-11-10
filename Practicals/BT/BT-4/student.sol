// SPDX-License-Identifier: MIT
pragma solidity >=0.7.0 <0.9.0;

contract StudentManagement {
    
    struct Student {
        int stud_id;
        string name;
        string department;
    }
    
    Student[] students;
    mapping(string => uint) private departmentCounts;

    function addStudent(int stud_id, string memory name, string memory department) public {
        students.push(Student(stud_id, name, department));
        departmentCounts[department]++;
    }

    function getStudent(int stud_id) public view returns (string memory, string memory) {
        for (uint i = 0; i < students.length; i++) {
            if (students[i].stud_id == stud_id) {
                return (students[i].name, students[i].department);
            }
        }
        return ("Name Not Found", "Department Not Found");
    }

    function getDepartmentCount(string memory department) public view returns (uint) {
        return departmentCounts[department];
    }
}
