import grpc

from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserRequest, CreateUserResponse
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import OpenDebitCardAccountRequest, OpenDebitCardAccountResponse
from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import AccountsGatewayServiceStub
from contracts.services.gateway.cards.rpc_issue_physical_card_pb2 import IssuePhysicalCardRequest, IssuePhysicalCardResponse
from contracts.services.gateway.cards.cards_gateway_service_pb2_grpc import CardsGatewayServiceStub
from tools.fakers import fake


channel = grpc.insecure_channel("localhost:9003")

users_gateway_service = UsersGatewayServiceStub(channel)
accounts_gateway_service = AccountsGatewayServiceStub(channel)
cards_gateway_service = CardsGatewayServiceStub(channel)

create_user_request = CreateUserRequest(
    email=fake.email(),
    last_name=fake.last_name(),
    first_name=fake.first_name(),
    middle_name=fake.middle_name(),
    phone_number=fake.phone_number()
)
create_user_response: CreateUserResponse = users_gateway_service.CreateUser(create_user_request)

open_debit_card_account_request = OpenDebitCardAccountRequest(user_id=create_user_response.user.id)
open_debit_card_account_response: OpenDebitCardAccountResponse = accounts_gateway_service.OpenDebitCardAccount(open_debit_card_account_request)

issue_physical_card_request = IssuePhysicalCardRequest(user_id=create_user_response.user.id, account_id=open_debit_card_account_response.account.id)
issue_physical_card_response: IssuePhysicalCardResponse = cards_gateway_service.IssuePhysicalCard(issue_physical_card_request)

print("Create user response:", create_user_response)
print("Open debit card account response:", open_debit_card_account_response)
print("Issue physical card response:", issue_physical_card_response)