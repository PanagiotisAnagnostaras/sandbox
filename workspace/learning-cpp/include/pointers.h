namespace pointersSchool
{
    class PointersSchool
    {
    public:
        PointersSchool();

    private:
        void helperFun(int pass_by_val, int* pass_by_ptr, int& pass_by_ref);
        void helperFunForNull(int);
        void helperFunForNull(int*);
    };
}