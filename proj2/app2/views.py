from django.shortcuts import render
from app2.forms import StudentForm

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'app2/index.html', {'form': StudentForm(), 'success': True})
    else:
        form = StudentForm()
    return render(request, 'app2/index.html', {'form': form})