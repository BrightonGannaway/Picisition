class Constants:

    class DetectNet:

        argv = ['ssd-mobilenet-v2', 'models/labels.txt', '--input-blob=input_0', '--output-cvg=scores', '--output-bbox=boxes']

        class Defaults:
            model = "model/ssd-mobilenet.onnx",
            labels = "model/labels.txt",
            input_blob = "input_0",
            output_cvg = "scores",
            output_bbox = "boxes",
            threshold = 0.5

    class GameLogic:

        class Defaults:
            goal = ""
            guesses = []
            closest_guess = None
            game_state = "not_started"
            score = 0
        
        class GameStates:
            NOT_STARTED = "not_started"
            IN_PROGRESS = "in_progress"
            COMPLETED = "completed"
            FAILED = "failed"

    class ModelAPI:
        
        class Defaults:
            model_prompt = ""
            base_url = "http://localhost:8080/api/chat/completions"
            headers = {
                "Content-Type": "application/json"
            }
            temperature = 0.2
            top_p = 0.95
            max_tokens = 1000
            stop_sequences = ["<end>"]

        class SystemPrompts:
            latest_working = "src/model/system_prompts/model_prompt.txt"
            default = "src/model/system_prompts/model_prompt.txt"
        

