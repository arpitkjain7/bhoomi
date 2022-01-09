# from sql.crud.user_roles_crud import CRUDUserRole
# from sql.crud.services_crud import CRUDServices
# from sql.crud.license_crud import CRUDLicense
# from sql.crud.user_crud import CRUDUser
# from sql.crud.cloud_config_crud import CRUDCloudConfig
# from sql.crud.user_transactions_crud import CRUDUserTransactions
# from sql.controllers.user_management.user_management_controller import (
#     UserManagementController,
# )
# from sql.apis.schemas.requests.user_management.user_request import Register
# from datetime import datetime


# def create_user_roles(user_role_record: list):
#     user_roles = CRUDUserRole().read_all()
#     if len(user_roles) == 0:
#         for item in user_role_record:
#             CRUDUserRole().create(**item)
#     else:
#         pass


# def create_services(supported_services: list):
#     existing_services = CRUDServices().read_all()
#     if len(existing_services) == 0:
#         for item in supported_services:
#             CRUDServices().create(**item)
#     else:
#         pass


# def create_license_records(supported_licenses: list):
#     existing_licenses = CRUDLicense().read_all()
#     if len(existing_licenses) == 0:
#         for item in supported_licenses:
#             CRUDLicense().create(**item)
#     else:
#         pass


# def create_admin_user(admin_user_request):
#     existing_admin_user = CRUDUser().read(user_name="admin")
#     if not existing_admin_user:
#         _ = UserManagementController().register_user_controller(
#             request=admin_user_request
#         )
#     else:
#         pass


# def create_admin_user_transactions(admin_user_transactions_request):
#     existing_profile_record = CRUDUserTransactions().read(user_name="admin")
#     if not existing_profile_record:
#         CRUDUserTransactions().create(**admin_user_transactions_request)
#     else:
#         pass


# def create_cloud_config(cloud_config_request):
#     existing_cloud_config = CRUDCloudConfig().read_all()
#     if len(existing_cloud_config) == 0:
#         for item in cloud_config_request:
#             CRUDCloudConfig().create(**item)
#     else:
#         pass


# def main():
#     user_role_record = [
#         {
#             "user_role": "admin",
#             "user_role_id": 1,
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#         {
#             "user_role": "editor",
#             "user_role_id": 2,
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#         {
#             "user_role": "viewer",
#             "user_role_id": 3,
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#     ]
#     create_user_roles(user_role_record=user_role_record)
#     supported_services = [
#         {
#             "service_name": "rekognition",
#             "use_case": "image_classification",
#             "cloud_service_provider": "aws",
#             "status": "active",
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#         {
#             "service_name": "rekognition",
#             "use_case": "face_detection",
#             "cloud_service_provider": "aws",
#             "status": "active",
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#         {
#             "service_name": "rekognition",
#             "use_case": "explicit_content_detection",
#             "cloud_service_provider": "aws",
#             "status": "active",
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#         {
#             "service_name": "rekognition",
#             "use_case": "face_mask_detection",
#             "cloud_service_provider": "aws",
#             "status": "active",
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#         {
#             "service_name": "comprehend",
#             "use_case": "dominant_language",
#             "cloud_service_provider": "aws",
#             "status": "active",
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#         {
#             "service_name": "comprehend",
#             "use_case": "natural_entity_recognition",
#             "cloud_service_provider": "aws",
#             "status": "active",
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#         {
#             "service_name": "comprehend",
#             "use_case": "sentiment_analysis",
#             "cloud_service_provider": "aws",
#             "status": "active",
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#         {
#             "service_name": "comprehend",
#             "use_case": "pos_tagging",
#             "cloud_service_provider": "aws",
#             "status": "active",
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#         {
#             "service_name": "comprehend",
#             "use_case": "pii_redaction",
#             "cloud_service_provider": "aws",
#             "status": "active",
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#         {
#             "service_name": "translate",
#             "use_case": "text_translation",
#             "cloud_service_provider": "aws",
#             "status": "active",
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#         {
#             "service_name": "translate",
#             "use_case": "async_text_translation",
#             "cloud_service_provider": "aws",
#             "status_check_function": "describe_text_translation_job",
#             "response_wrapper": "TextTranslationJobProperties",
#             "status": "active",
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#         {
#             "service_name": "transcribe",
#             "use_case": "async_audio_transcription",
#             "cloud_service_provider": "aws",
#             "status": "active",
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#         {
#             "service_name": "polly",
#             "use_case": "text_to_speech",
#             "cloud_service_provider": "aws",
#             "status": "active",
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#         {
#             "service_name": "polly",
#             "use_case": "async_text_to_speech",
#             "cloud_service_provider": "aws",
#             "status_check_function": "get_speech_synthesis_task",
#             "response_wrapper": "SynthesisTask",
#             "status": "active",
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#         {
#             "service_name": "textract",
#             "use_case": "ocr",
#             "cloud_service_provider": "aws",
#             "status": "active",
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#         {
#             "service_name": "textract",
#             "use_case": "text_extraction",
#             "cloud_service_provider": "aws",
#             "status": "active",
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#         {
#             "service_name": "fraud_detector",
#             "use_case": "fraud_detection",
#             "cloud_service_provider": "aws",
#             "status": "active",
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#         {
#             "service_name": "forecast",
#             "use_case": "forecasting",
#             "cloud_service_provider": "aws",
#             "status": "active",
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#         {
#             "service_name": "lookout",
#             "use_case": "analomy_detection",
#             "cloud_service_provider": "aws",
#             "status": "active",
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#         {
#             "service_name": "comprehend",
#             "use_case": "async_document_classification",
#             "cloud_service_provider": "aws",
#             "status_check_function": "describe_document_classification_job",
#             "response_wrapper": "DocumentClassificationJobProperties",
#             "status": "active",
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#         {
#             "service_name": "comprehend",
#             "use_case": "async_dominant_language_detection",
#             "cloud_service_provider": "aws",
#             "status_check_function": "describe_dominant_language_detection_job",
#             "response_wrapper": "DominantLanguageDetectionJobProperties",
#             "status": "active",
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#         {
#             "service_name": "comprehend",
#             "use_case": "async_entity_detection",
#             "cloud_service_provider": "aws",
#             "status_check_function": "describe_entities_detection_job",
#             "response_wrapper": "EntitiesDetectionJobProperties",
#             "status": "active",
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#         {
#             "service_name": "comprehend",
#             "use_case": "async_pii_detection",
#             "cloud_service_provider": "aws",
#             "status_check_function": "describe_pii_entities_detection_job",
#             "response_wrapper": "PiiEntitiesDetectionJobProperties",
#             "status": "active",
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#         {
#             "service_name": "comprehend",
#             "use_case": "async_sentiment_detection",
#             "cloud_service_provider": "aws",
#             "status_check_function": "describe_sentiment_detection_job",
#             "response_wrapper": "SentimentDetectionJobProperties",
#             "status": "active",
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#         {
#             "service_name": "comprehend",
#             "use_case": "async_topic_detection",
#             "cloud_service_provider": "aws",
#             "status_check_function": "describe_topics_detection_job",
#             "response_wrapper": "TopicsDetectionJobProperties",
#             "status": "active",
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#         {
#             "service_name": "textract",
#             "use_case": "async_document_analysis",
#             "cloud_service_provider": "aws",
#             "status_check_function": "get_document_analysis",
#             "response_wrapper": "Blocks",
#             "status": "active",
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#         {
#             "service_name": "textract",
#             "use_case": "async_document_text_detection",
#             "cloud_service_provider": "aws",
#             "status_check_function": "get_document_text_detection",
#             "response_wrapper": "Blocks",
#             "status": "active",
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#         {
#             "service_name": "textract",
#             "use_case": "async_expense_analysis",
#             "cloud_service_provider": "aws",
#             "status_check_function": "get_expense_analysis",
#             "response_wrapper": "Blocks",
#             "status": "active",
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#     ]
#     create_services(supported_services=supported_services)
#     supported_license = [
#         {
#             "license_type": "basic",
#             "api_limit": 5,
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#         {
#             "license_type": "teams",
#             "api_limit": 20,
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#         {
#             "license_type": "enterprise",
#             "api_limit": 1000,
#             "created_at": datetime.now(),
#             "updated_at": datetime.now(),
#         },
#     ]
#     create_license_records(supported_licenses=supported_license)
#     admin_user_request = Register(
#         user_name="admin",
#         password="P@ssw0rd",
#         full_name="Admin User",
#         email_id="admin@noahsark.com",
#         license_type="basic",
#         user_role="admin",
#         user_role_id=1,
#     )
#     admin_user_transactions_request = {
#         "user_name": "admin",
#         "transactional_details": {},
#     }
#     create_admin_user(admin_user_request=admin_user_request)
#     create_admin_user_transactions(
#         admin_user_transactions_request=admin_user_transactions_request
#     )
#     default_cloud_config = [
#         {"config_parameter": "gcp_project_id"},
#         {"config_parameter": "aws_role_arn"},
#         {"config_parameter": "gcp_region", "config_value": "us-central1"},
#         {"config_parameter": "aws_region", "config_value": "us-east-1"},
#         {"config_parameter": "testing_env", "config_value": "local"},
#         {"config_parameter": "queue_url"},
#     ]
#     create_cloud_config(cloud_config_request=default_cloud_config)
