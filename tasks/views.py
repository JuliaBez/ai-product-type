from rest_framework import viewsets

from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.http import HttpResponse
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import Task
from .serializers import TaskSerializer
import g4f

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer

    @action(detail=False, methods=['get'])
    def filter_by_date(self, request):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        tasks = self.queryset
        if start_date and end_date:
            tasks = tasks.filter(due_date__range=[start_date, end_date])
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)

def export_tasks_pdf(request):
    buffer = BytesIO()
    pdf_canvas = canvas.Canvas(buffer, pagesize=letter)
    pdf_canvas.setFont("Helvetica", 12)

    tasks = Task.objects.all()

    pdf_canvas.drawString(100, 750, "Tasks for the Current Month:")
    y = 720

    for task in tasks:
        line = f"Title: {task.title}, Due Date: {task.due_date}, Status: {task.status}"
        pdf_canvas.drawString(100, y, line)
        y -= 20
        if y < 50:
            pdf_canvas.showPage()
            pdf_canvas.setFont("Helvetica", 12)
            y = 750

    pdf_canvas.save()
    buffer.seek(0)
    return HttpResponse(buffer, content_type="application/pdf")


def load_resume():
    resume_path = "/home/julia/taskmanager/resume.txt"
    try:
        with open(resume_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        return f"Error loading resume: {str(e)}"

resume_text = load_resume()

@api_view(['POST'])
def chatbot_response(request):
    user_question = request.data.get("message", "").lower()

    negative_keywords = ["bad", "weakness", "worst", "negative", "fail", "mistake", "problem", "flaw", "issue", "red flag"]

    if any(word in user_question for word in negative_keywords):
        answer = (
            "Julia's only 'flaw' is her extreme dedication to work! "
        )
    else:
        prompt = f"""
        You are Jul-IA, an AI assistant helping recruiters understand why Julia Bez Batti Viana is the best fit for this Full-Stack Developer job. 
        The role requires expertise in React, Next.js, Python, TypeScript, and integrations. 
        Always focus on positive aspects.

        Julia's resume:
        {resume_text}

        User Question: {user_question}
        """

        try:
            response = g4f.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )

            answer = response if isinstance(response, str) else response.get("choices", [{}])[0].get("text", "Error generating response.")

        except Exception as e:
            print(f"Chatbot Error: {str(e)}")
            answer = "Oops, something went wrong. But you should definitely hire Julia!"

    return Response({"response": answer})
