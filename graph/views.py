from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import json

def mainpage(request):
    if request.method == 'GET':
        t = get_template('test.html')
        html=t.render(Context({}))
        return HttpResponse(html)
    else:
        colours = range(9)
        data = request.POST.get('data')
        adjancencyList = json.loads(data)
        colouredVertex = [-1]*len(adjancencyList)
        for i in range(len(adjancencyList)):
            vertex = adjancencyList[i]
            choosedColours = []
            for adjacent in vertex:
                #a = 10
                choosedColours.append(colouredVertex[adjacent])
            remainingColours = []
            for colour in colours:
                if colour not in choosedColours:
                    remainingColours.append(colour)
            colouredVertex[i]=remainingColours[0]
		
        return HttpResponse(json.dumps(colouredVertex))
