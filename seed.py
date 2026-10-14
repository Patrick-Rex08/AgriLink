"""
AgriLink - Safe Database Demo Seeder
Seeds sample farmer crop listings and buyer orders without wiping existing user records.
Sample records are clearly prefixed with [Demo].
"""
import sys
import os

# Add backend directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.core.database import SessionLocal, init_db
from app.models.marketplace import CropBatch, BuyerOrder
from app.api.v1.endpoints.listings import SAMPLE_DEMO_BATCHES

def run_seed(force: bool = False):
    init_db()
    if SessionLocal is None:
        print("Database not configured.")
        return

    db = SessionLocal()
    try:
        existing_count = db.query(CropBatch).count()
        print(f"Current listings in database: {existing_count}")

        if existing_count > 0 and not force:
            print("Database already contains records. Skipping seed (use --force to seed anyway).")
            return

        added_batches = 0
        for item in SAMPLE_DEMO_BATCHES:
            exists = db.query(CropBatch).filter(CropBatch.batch_id == item["batch_id"]).first()
            if not exists:
                b = CropBatch(
                    batch_id=item["batch_id"],
                    farmer_name=item["farmer_name"],
                    farmer_phone=item["farmer_phone"],
                    crop_name=item["crop_name"],
                    variety=item["variety"],
                    category=item["category"],
                    quantity_kg=item["quantity_kg"],
                    available_qty_kg=item["quantity_kg"],
                    price_per_kg=item["price_per_kg"],
                    farm_location=item["farm_location"],
                    harvest_date=item["harvest_date"],
                    quality_grade=item["quality_grade"],
                    status="LISTED"
                )
                db.add(b)
                added_batches += 1

        db.commit()
        print(f"Successfully seeded {added_batches} demonstration crop listings.")

        existing_orders = db.query(BuyerOrder).count()
        if existing_orders == 0 or force:
            demo_order = BuyerOrder(
                order_id="ORD-DEMO-001",
                batch_id="BATCH-DEMO-WHT-001",
                buyer_name="[Demo] AgroMarts Wholesale",
                buyer_phone="9876501234",
                crop_name="Wheat",
                required_qty_kg=1000.0,
                fulfilled_qty_kg=1000.0,
                max_price_per_kg=26.50,
                total_price=26500.0,
                delivery_location="Azadpur Mandi, Delhi",
                status="In Transit"
            )
            db.add(demo_order)
            target = db.query(CropBatch).filter(CropBatch.batch_id == "BATCH-DEMO-WHT-001").first()
            if target:
                target.available_qty_kg = max(0.0, target.available_qty_kg - 1000.0)
            db.commit()
            print("Successfully seeded 1 demonstration buyer order.")

    except Exception as e:
        db.rollback()
        print(f"Seeding failed: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    force_flag = "--force" in sys.argv
    run_seed(force=force_flag)
