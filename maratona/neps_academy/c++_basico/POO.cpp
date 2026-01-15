
class Student
{
    public:

        // Atributos
        int id, age;
        int numberTests;
        double sumGrades;

        // Construtores
        Student(int _age, int _id, int _numberTests, double _sumGrades)
        {
            id = _id;
            age = _age;
            numberTests = _numberTests;
            sumGrades = _sumGrades;
        }

        // Métodos
        double getGradesAverage()
        {
            double average = sumGrades/numberTests;
            return average;
        }
};
