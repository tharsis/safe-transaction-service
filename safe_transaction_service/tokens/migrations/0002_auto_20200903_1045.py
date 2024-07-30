# Generated by Django 3.0.9 on 2020-09-03 10:45

from django.db import migrations, models

from eth_abi.exceptions import DecodingError
from web3.exceptions import Web3Exception

from gnosis.eth import get_auto_ethereum_client


def fix_token_decimals(apps, schema_editor):
    Token = apps.get_model("tokens", "Token")
    ethereum_client = get_auto_ethereum_client()

    for token in Token.objects.filter(decimals=0):
        try:
            decimals = ethereum_client.erc20.get_decimals(token.address)
            if decimals != token.decimals:
                token.decimals = decimals
                token.save(update_fields=["decimals"])
        except (Web3Exception, DecodingError, ValueError):
            token.decimals = None
            token.save(update_fields=["decimals"])


class Migration(migrations.Migration):
    dependencies = [
        ("tokens", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="token",
            name="spam",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="token",
            name="decimals",
            field=models.PositiveSmallIntegerField(
                blank=True, db_index=True, null=True
            ),
        ),
        migrations.RunPython(
            fix_token_decimals, reverse_code=migrations.RunPython.noop
        ),
    ]
