from datetime import datetime

class SimpleUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            path = request.path
            ip = request.META.get('REMOTE_ADDR')
            print(f"[{current_time}] {request.user.email} visited {path} from IP: {ip}")

        response = self.get_response(request)
        return response
