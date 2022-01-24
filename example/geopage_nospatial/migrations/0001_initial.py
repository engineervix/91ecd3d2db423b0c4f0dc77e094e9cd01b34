# Generated by Django 3.2.11 on 2022-01-24 19:05

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtailgeowidget.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0066_collection_management_permissions"),
    ]

    operations = [
        migrations.CreateModel(
            name="StandardPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("address", models.CharField(blank=True, max_length=250, null=True)),
                ("location", models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="StandardPageWithZoom",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("address", models.CharField(blank=True, max_length=250, null=True)),
                ("location", models.CharField(blank=True, max_length=250, null=True)),
                ("zoom", models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="StreamPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "body",
                    wagtail.core.fields.StreamField(
                        [
                            ("map", wagtailgeowidget.blocks.GeoBlock()),
                            (
                                "map_struct",
                                wagtail.core.blocks.StructBlock(
                                    [
                                        (
                                            "address",
                                            wagtail.core.blocks.CharBlock(
                                                required=True
                                            ),
                                        ),
                                        (
                                            "map",
                                            wagtailgeowidget.blocks.GeoBlock(
                                                address_field="address"
                                            ),
                                        ),
                                    ],
                                    icon="user",
                                ),
                            ),
                            (
                                "map_struct_with_zoom",
                                wagtail.core.blocks.StructBlock(
                                    [
                                        (
                                            "address",
                                            wagtailgeowidget.blocks.GeoAddressBlock(
                                                required=True
                                            ),
                                        ),
                                        (
                                            "zoom",
                                            wagtailgeowidget.blocks.GeoZoomBlock(
                                                required=False
                                            ),
                                        ),
                                        (
                                            "map",
                                            wagtailgeowidget.blocks.GeoBlock(
                                                address_field="address",
                                                zoom_field="zoom",
                                            ),
                                        ),
                                    ],
                                    icon="user",
                                ),
                            ),
                        ]
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]
