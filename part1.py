


class UpdateTasks(generics.GenericAPIView):
    serializer_class = ActiveTaskV2Serializer

    @swagger_auto_schema(request_body=ChangeTasksStatusSerializer,
                         responses={'200': ReadOnlyActiveTaskV2Serializer(many=True)})
    def patch(self, request, *args, **kwargs):
        task_status = self.kwargs.get('status')
        serializer = ChangeTasksStatusSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            task_tracking_ids = serializer.data.get('task_tracking_ids', [])
            additional_time = serializer.data.get('additional_time', TaskActiveV2.default_additional_time_in_seconds)

            if (task_status == StatusTypes.DEFERRED.value or task_status == StatusTypes.QUEUED.value):
                is_updated, data = defer_resume_tasks_helper(email, task_tracking_ids, additional_time, task_status)
            elif (task_status == StatusTypes.KILLABLE.value):
                is_updated, data = kill_tasks_helper(email, task_tracking_ids, task_status)
            elif (task_status == StatusTypes.DELETED.value):
                is_updated, data = delete_tasks_helper(email, task_tracking_ids)

            if is_updated and not data:
                return Response(status=status.HTTP_200_OK, data=data)
            elif is_updated and data:
                return Response(status=status.HTTP_412_PRECONDITION_FAILED, data=data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND, data=data)

        return Response(status=status.HTTP_400_BAD_REQUEST, data=[])



# Target interface
class Target:
    def request(self):
        pass

# Adaptee class with an incompatible interface
class Adaptee:
    def specific_request(self):
        print("Adaptee's specific request")

# Adapter class that makes Adaptee compatible with Target
class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        self.adaptee.specific_request()

# Client code
adaptee = Adaptee()
adapter = Adapter(adaptee)
adapter.request()




# Adaptee: EuropeanSocket
class EuropeanSocket:
    def plug(self, voltage):
        print(f"European socket plugged in with {voltage}V")

# Target: NorthAmericanSocket (the interface expected by the client)
class NorthAmericanSocket:
    def plug(self, voltage):
        pass

# Adapter: EuropeanToNorthAmericanAdapter
class EuropeanToNorthAmericanAdapter(NorthAmericanSocket):
    def __init__(self, european_socket):
        self.european_socket = european_socket

    def plug(self, voltage):
        # Convert the European voltage to North American voltage (e.g., 220V to 110V)
        voltage /= 2
        self.european_socket.plug(voltage)

# Client code
european_socket = EuropeanSocket()
adapter = EuropeanToNorthAmericanAdapter(european_socket)

# Now, the client can use the North American socket interface
adapter.plug(220)  # The adapter converts the voltage and plugs into the European socket

