from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedAccountsPlan, SeedCardsPlan, SeedOperationsPlan


class ExistingUserGetOperationsSeedsScenario(SeedsScenario):
    """
    Сценарий сидинга для существующего пользователя, который имеет кредитный счет и операции по этому счету.
    Создаём 300 пользователей, каждому из которых открываются кредитный счёт.
    """
    @property
    def plan(self) -> SeedsPlan:
        """
        Возвращает план сидинга для создания пользователей и их счетов.
        Мы создаём 300 пользователей, каждый получит кредитный счёт и
        операции покупки, пополнения счета, снятия наличных по этому счету.
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=300,
                credit_card_accounts=SeedAccountsPlan(
                    count=1,
                    purchase_operations=SeedOperationsPlan(count=5),
                    transfer_operations=SeedOperationsPlan(count=1),
                    cash_withdrawal_operations=SeedOperationsPlan(count=1)
                )
            )
        )

    @property
    def scenario(self) -> str:
        """
        Возвращает название сценария сидинга.
        Это имя будет использоваться для сохранения данных сидинга.
        """
        return "existing_user_get_operations"


if __name__ == '__main__':
    """
    Запуск сценария сидинга вручную.
    Создаём объект сценария и вызываем метод build для создания данных.
    """
    seeds_scenario = ExistingUserGetOperationsSeedsScenario()
    seeds_scenario.build()